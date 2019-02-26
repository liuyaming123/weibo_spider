# -*-coding:utf-8-*-

from bs4 import BeautifulSoup as Soup
import requests
import json,os,time
from pymongo import MongoClient

'''
免费西刺ip抓取
'''

# 导入配置文件
config = json.load(open(os.sep.join(['conf','conf.json']), 'r'))
conn = MongoClient(config["mongodb_conn"]["name"])
ip_xici = conn.ip_info.ip_xici


header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/64.0.3282.186 Safari/537.36'}

def dict2proxy(dic):
    s = dic['type'] + '://' + dic['ip'] + ':' + str(dic['port'])
    return {'http': s, 'https': s}

def parse_items(items):
    # 存放ip信息字典的列表
    ips = []
    for item in items:
        tds = item.find_all('td')
        # 从对应位置获取ip，端口，类型
        ip, port, _type = tds[1].text, int(tds[2].text), tds[5].text
        ips.append({'ip': ip, 'port': port, 'type': _type})
    return ips

# 检查ip可用性
def check_ip(ip):
    try:
        proxy = dict2proxy(ip)
        url = 'https://www.ipip.net/'
        r = requests.get(url, headers=header, proxies=proxy,timeout=5)
        r.raise_for_status()     # 如果请求错误，可以用Response.raise_for_status()来抛出异常
    except:
        return False
    else:
        return True

# 使id自增
def id_auto_increase(coll):
    try:
        id = int(coll.find().sort('_id', -1).limit(1)[0]['_id'])+1
    except Exception as e:
        print(e)
        print('The query sequence number( _id ) failed and the sequence number was inserted from scratch')
        id = 1
    return id



def get_proxies(index=1):
    url = 'http://www.xicidaili.com/nt/%d' % index
    r = requests.get(url, headers=header)
    r.encoding = r.apparent_encoding
    r.raise_for_status()
    soup = Soup(r.text, 'lxml')
    # 第一个是显示最上方的信息的，需要丢掉
    items = soup.find_all('tr')[1:]
    ips = parse_items(items)
    for ip in ips:
        if check_ip(ip):
            print(ip)
            _id = id_auto_increase(ip_xici)
            ip_xici.update({'_id': _id}, {
                            '$set': {'ip': ip.get('ip'),'port': ip.get('port'),'type': ip.get('type'), 'crawl_time': int(time.time())}}, upsert=True)

if __name__ == '__main__':
    for i in range(1,21):
        get_proxies(i)
