# -*- coding:utf-8 -*-

import json
import random
import traceback
import requests
import re
import time
import os
from multiprocessing import Pool
from util import headers, ip_item
from pymongo import MongoClient


'''微博评论爬取'''


# 导入配置文件
config = json.load(open(os.sep.join(['conf','conf.json']), 'r'))

# 日志文件地址
log_file_path = "{}/logs/".format(config["logs_path"])
lf_error = "{}/{}.log".format(log_file_path, time.strftime('error_{}_%Y'.format('107603'), time.localtime()))

# mongo库表
conn = MongoClient(config["mongodb_conn"]["name"])
weibo_user = conn.weibo_info.weibo_user
weibo_topic = conn.weibo_info.weibo_topic
weibo_topic.ensure_index('weibo_id', unique=True)
weibo_comment = conn.weibo_info.weibo_comment  # 创建库表



class Weibo_Spider():
    def __init__(self, oid):
        self.headers = headers()
        self.lf_comment = "{}/{}.log".format(log_file_path,time.strftime('comment_{}_%Y-%m-%d'.format(oid), time.localtime()))  # 评论日志路径
        self.index_id = 0    # 获取mongo里的代理ip用
        self.name = self.get_name(oid)
        self.tags = re.compile('</?\w+[^>]*>')  # 找到html标签

    def dict2proxy(self,dic):
        s = dic['type'] + '://' + dic['ip'] + ':' + str(dic['port'])
        return {'http': s, 'https': s}

    def proxy(self):
        ip, port, type= ip_item[self.index_id].get('ip'),ip_item[self.index_id].get('port'),ip_item[self.index_id].get('type')
        proxy = self.dict2proxy({'ip': ip, 'port': port, 'type': type})
        return proxy

    def detail_p(self,id):
        '''
        爬取评论
        :param id: 话题id
        :return: None
        '''
        base_url = 'https://m.weibo.cn/api/comments/show?id=' + id + '&page={page}'

        index = 1
        while 1:
            # print('正在爬取用户-----> '+self.name+' <-----当前微博的第%s页comment-------------------------------------------------------------------------' % (index))
            try:
                url = base_url.format(page=index)
                index += 1

                while 1:
                    try:
                        resp = requests.get(url, headers=self.headers,proxies = self.proxy(),timeout = 3)
                        print('proxies2:',self.proxy())
                        resp.raise_for_status()
                    except:
                        self.index_id += 1
                        if self.index_id == 39:
                            self.index_id = 0
                    else:
                        break

                resp.encoding = 'utf-8'
                jsondata = resp.json()
                if not jsondata.get("ok"):
                    break
                time.sleep(random.randint(2,3))
                data = jsondata.get('data').get('data')
                for d in data:
                    try:
                        _id = d.get('id')
                        weibo_id = id
                        created_at = d.get('created_at')
                        source = d.get('source')
                        user = d.get('user')
                        text = d.get('text')
                        reply_id = d.get('reply_id')
                        reply_text = d.get('reply_text')
                        like_counts = d.get('like_counts')
                        liked = d.get('liked')

                        # 入库
                        weibo_comment.insert({'_id': _id, 'weibo_id': weibo_id, 'comment_api': url, 'created_at': created_at,
                                     'source': source, 'user': user, 'text': text,
                                     'reply_id': reply_id, 'reply_text': reply_text, 'like_counts': like_counts,
                                     'liked': liked, 'crawl_time': int(time.time())})

                        # 写日志
                        username = d.get("user").get("screen_name")
                        if '<' in text:
                            text = self.tags.sub('', d.get("text"))    # 用正则找到html标签并替换为空串
                        cont = 'comment===' + username + ': ' + text
                        self.log(cont,self.lf_comment)

                    except Exception:
                        self.log(traceback.format_exc(), lf_error)
                print('\n')
            except Exception:
                self.log(traceback.format_exc(),lf_error)


    def get_user_comments(self,oid,containerid):
        '''
        获取话题id
        :param containerid: 内容id
        :return: None
        '''
        index_page = 1
        while 1:
            url = 'https://m.weibo.cn/api/container/getIndex?containerid='+containerid+'_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page='+str(index_page)

            while 1:
                try:
                    resp = requests.get(url, headers=self.headers, proxies=self.proxy(), timeout=3)
                    resp.raise_for_status()
                except:
                    self.index_id += 1
                    if self.index_id == 39:
                        self.index_id = 0
                else:
                    break

            resp.encoding = 'utf-8'
            resp = resp.json()
            if not resp.get("ok"):
                break
            time.sleep(random.randint(2,6))
            jsondata = resp["data"]["cards"]
            # weibo_cnt = resp["data"]["cardlistInfo"]["total"]
            # if index_page == 1:
                # print('当前爬取的用户为---> '+self.name+' <---该用户当前的微博条数为%s条\n\n\n\n'%weibo_cnt)
            for da in jsondata:
                try:
                    topic_id = da.get("mblog").get("id")   # 话题id
                    topic = da.get("mblog").get("text")  # 每一条话题的内容
                    if '<' in topic:
                        topic = self.tags.sub('', topic)
                    weibo_topic.update_one({'weibo_id': topic_id}, {'$set': {'oid': oid, 'topic': topic,'create_time': int(time.time())}}, upsert=True)
                    print("正在爬取微博：" + topic)

                    # 增量爬
                    if weibo_comment.find_one({'weibo_id': topic_id}):
                        print('该微博内容已爬取，正在过滤...\n')
                        break

                    if topic_id:
                        self.detail_p(topic_id)

                except AttributeError:
                    pass
                except Exception:
                    self.log(traceback.format_exc(), lf_error)
            index_page += 1

    def get_name(self,oid):
        url = 'https://m.weibo.cn/api/container/getIndex?containerid=100505' + oid
        jd = requests.get(url, self.headers).json()
        weibo_name = jd.get('data').get('userInfo').get('screen_name')
        return weibo_name

    # 日志
    def log(self, text="", log_file=""):
        if not os.path.isdir(log_file_path):
            os.makedirs(log_file_path)
        log = "[{}] [info:{}]".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), text)
        with open(log_file, "a+", encoding='utf-8') as f:
            f.write(log + "\n")



# 用户唯一标志：oid

# oid = '1655665171'  # 崔玉涛
# oid = '2623922575'  # 刘晓雁医生
# oid = '1945390842'  # 育学园儿科医生涂绘玲
# oid = '5662555038'  # 儿科医生赵涓
# oid = '5810945254'  # 儿科医生崔咏望
# oid = '6387770246'  # 儿科医生宫红梅
# oid = '3538883541'  # 张亚停医生
# oid = '2769301163'  # 蓬蕊医生
# oid = '5575084454'  # 和睦家儿科刘华医生
# oid = '1396626753'  # 育儿专家-王玉玮
# oid = '1557303822'  # 儿科医生鱼小南
# oid = '1086782701'  # 虾米妈咪
# oid = '1893410897'  # 鲍秀兰诊室
# oid = '2399301482'  # 医生妈妈欧茜

oids = ['1655665171','2623922575','1945390842','5662555038','5810945254','6387770246','3538883541','2769301163','5575084454','1396626753',
        '1557303822','1086782701','1893410897','2399301482',]


def main(oid):
    containerid = '107603' + oid
    main_page = 'https://m.weibo.cn/u/' + oid
    spider = Weibo_Spider(oid)
    weibo_name = spider.get_name(oid)
    weibo_user.update_one({'oid': oid},{'$set': {'weibo_name': weibo_name, 'main_page': main_page, 'create_time': int(time.time())}},upsert=True)
    spider.get_user_comments(oid,containerid)


if __name__=='__main__':
    p=Pool(10)  # 创建进程池和进程的数量
    for oid in oids:
        p.apply_async(func=main,args=(oid,))
    p.close()
    p.join()