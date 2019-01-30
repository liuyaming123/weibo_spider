# -*- coding:utf-8 -*-

import json
import random
import traceback
import requests
import re
import time
import os


'''微博评论爬取'''


# 导入配置文件
conf_dir = os.sep.join(['conf','conf.json'])
f = open(conf_dir, 'r')
config = json.load(f)

# 日志文件地址
log_file_path = "{}/logs/".format(config["logs_path"])



class Weibo_Spider():
    def __init__(self):
        self.headers = {
                        'accept': 'application/json, text/plain, */*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'zh-CN,zh;q=0.9',
                        'cookie': '_T_WM=a0a021eb13474d690ca4930c7ec5e67b; H5_wentry=H5; ALF=1550717165; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W56HfnxVzTy7OHy0Eu_vUuF5JpX5K-hUgL.FoqpS02ES0zR1hz2dJLoIpMLxK-LB.-L1K5LxK.L1KnLBoeceo.7S5tt; WEIBOCN_WM=3349; backURL=https%3A%2F%2Fm.weibo.cn%2Fapi%2Fcomments%2Fshow%3Fid%3D4331511564696861%26page%3D5; WEIBOCN_FROM=1110106030; MLOGIN=1; XSRF-TOKEN=d9bbe8; SCF=Ag4PfcUwfHKHYXb-Ol1ygOEByeFeJp4U86hef00lBij7kJZzlnXx3e_8AlfvKp237ADIJ1u4--NxlbGBLAu1BYo.; SUB=_2A25xTHkiDeRhGeBP7FMT9yzEwz6IHXVSzwdqrDV6PUJbkdAKLUHykW1NRSlLmwrMFhpqjw0g75zjrdc1rzH0P7Ip; SUHB=0U1JV78LYFfLjg; SSOLoginState=1548224882; M_WEIBOCN_PARAMS=oid%3D4331511564696861%26lfid%3D1076032701177800%26luicode%3D20000174',
                        'mweibo-pwa': '1',
                        'referer': 'https://m.weibo.cn/detail/4331511564696861?sudaref=login.sina.com.cn',
                        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3554.0 Safari/537.36',
                        'x-requested-with': 'XMLHttpRequest'
                    }
        self.name = self.get_name(oid)
        self.tags = re.compile('</?\w+[^>]*>')  # 找到html标签

    def detail_p(self,id):
        '''
        爬取评论
        :param id: 话题id
        :return: None
        '''
        base_url = 'https://m.weibo.cn/api/comments/show?id=' + id + '&page={page}'

        index = 1
        while 1:
            print('正在爬取用户-> '+self.name+' <-当前微博的第%s页comment-------------------------------------------------------------------------' % (index))
            try:
                url = base_url.format(page=index)
                index += 1
                resp = requests.get(url, headers=self.headers)
                resp.encoding = 'utf-8'
                jsondata = resp.json()
                if not jsondata.get("ok"):
                    print('\n')
                    break
                print(url)
                time.sleep(random.randint(1,2))
                data = jsondata.get('data').get('data')
                for d in data:
                    try:
                        username, text = d.get("user").get("screen_name"), d.get('text')
                        if '<' in text:
                            text = self.tags.sub('', d.get("text"))    # 用正则找到html标签并替换为空串
                        cont = 'comment===' + username + ': ' + text
                        self.log(cont,lf_comment)
                        print(cont)
                    except Exception:
                        self.log(traceback.format_exc(),lf_error)
                print('\n')
            except Exception as e:
                print(e)
                self.log(traceback.format_exc(),lf_error)


    def get_user_comments(self,containerid):
        '''
        获取话题id
        :param containerid: 内容id
        :return: None
        '''
        index_page = 1
        cnt = 1    # 统计爬取评论的数量
        while 1:
            url = 'https://m.weibo.cn/api/container/getIndex?containerid='+containerid+'_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page='+str(index_page)
            resp = requests.get(url,headers=self.headers)
            resp.encoding = 'utf-8'
            resp = resp.json()
            if not resp.get("ok"):
                print(resp.get("msng"))
                break
            time.sleep(random.randint(1,2))
            jsondata = resp["data"]["cards"]
            weibo_cnt = resp["data"]["cardlistInfo"]["total"]
            if index_page == 1:
                print('当前爬取的用户为---> '+self.name+' <---该用户当前的微博条数为%s条\n\n\n\n'%weibo_cnt)
            for da in jsondata:
                # print('da:',da)
                try:
                    topic_id = da["mblog"]["id"]   # 话题id
                    topic = da["mblog"]["text"]  # 每一条话题的内容
                    if '<' in topic:
                        topic = self.tags.sub('', topic)
                    print("正在爬取第%s条微博："%(cnt) + topic)
                    if topic_id:
                        self.detail_p(topic_id)
                    cnt += 1
                    time.sleep(random.randint(1,2))
                except Exception:
                    self.log(traceback.format_exc(), lf_error)
                    # print('da:',da)
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



if __name__ == '__main__':
    # 用户唯一标志：oid
    # oid = '1662214194'  # 北京人不知道的北京事儿
    # oid = '1742987497'  # 上海地铁
    # oid = '1655665171'  # 崔玉涛
    # oid = '1361074815'  # 古天乐

    oids = ['1655665171',]

    for oid in oids:
        containerid = '107603' + oid

        # 日志路径
        lf_comment = "{}/{}.log".format(log_file_path,time.strftime('comment_{}_%Y-%m-%d'.format(containerid+'-----'), time.localtime()))  # 评论日志路径
        lf_error = "{}/{}.log".format(log_file_path, time.strftime('error_{}_%Y'.format('107603'), time.localtime()))

        # main
        spider = Weibo_Spider()
        spider.get_user_comments(containerid)





