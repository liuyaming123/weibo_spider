# -*-coding:utf-8-*-

import time



header1 = {
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': '_T_WM=68cfde42e5edabdb52f6f86dff7a1b0e; WEIBOCN_FROM=1110105030; SUB=_2A25xdQIGDeRhGeBH7FEY9S3LyTyIHXVSma5OrDV6PUJbkdANLWT1kW1NQac6rVR8X4H1PDA-BabvgstMAsVEFcjO; SUHB=0pHBkoo6kdKw_W; SCF=AnDXYw-rrHvOhMb3N85asXDr5ARR4OtIQWQjgZ8SuTySS9415joSp0UNJvleIYEQAhzlX_komSELrTW8nw5-nbE.; SSOLoginState=1550938710; MLOGIN=1; XSRF-TOKEN=5b943e; M_WEIBOCN_PARAMS=luicode%3D20000174%26uicode%3D10000011%26fid%3D2304131655665171_-_WEIBO_SECOND_PROFILE_WEIBO',
            'mweibo-pwa': '1',
            'referer': 'https://m.weibo.cn/p/2304131655665171_-_WEIBO_SECOND_PROFILE_WEIBO',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
         }

header2 = {
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': '_T_WM=68cfde42e5edabdb52f6f86dff7a1b0e; WEIBOCN_FROM=1110006030; SUB=_2A25xdRVoDeRhGeBP7FMT9yzEwz6IHXVSmbsgrDV6PUJbkdAKLRf1kW1NRSlLmyi5QoHgPEf94DgeTcbh1dawxbWw; SUHB=0oUog-tiIax4mG; SCF=Ar2taBAhP2_wBG9x-yVQSiiTavA0udUHj9xghJornEOWP-5PIAvigvW317gOXk0u6BJ8m6a57JWdB-63t7S1mdI.; SSOLoginState=1550935352; MLOGIN=1; XSRF-TOKEN=76d073; M_WEIBOCN_PARAMS=uicode%3D20000061%26fid%3D4342851003690679%26oid%3D4342851003690679',
            'mweibo-pwa': '1',
            'referer': 'https://m.weibo.cn/detail/4342851003690679',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
         }

header3 = {
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': '_T_WM=a0a021eb13474d690ca4930c7ec5e67b; H5_wentry=H5; ALF=1550717165; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W56HfnxVzTy7OHy0Eu_vUuF5JpX5K-hUgL.FoqpS02ES0zR1hz2dJLoIpMLxK-LB.-L1K5LxK.L1KnLBoeceo.7S5tt; WEIBOCN_WM=3349; backURL=https%3A%2F%2Fm.weibo.cn%2Fapi%2Fcomments%2Fshow%3Fid%3D4331511564696861%26page%3D5; WEIBOCN_FROM=1110106030; MLOGIN=1; XSRF-TOKEN=d9bbe8; SCF=Ag4PfcUwfHKHYXb-Ol1ygOEByeFeJp4U86hef00lBij7kJZzlnXx3e_8AlfvKp237ADIJ1u4--NxlbGBLAu1BYo.; SUB=_2A25xTHkiDeRhGeBP7FMT9yzEwz6IHXVSzwdqrDV6PUJbkdAKLUHykW1NRSlLmwrMFhpqjw0g75zjrdc1rzH0P7Ip; SUHB=0U1JV78LYFfLjg; SSOLoginState=1548224882; M_WEIBOCN_PARAMS=oid%3D4331511564696861%26lfid%3D1076032701177800%26luicode%3D20000174',
            'mweibo-pwa': '1',
            'referer': 'https://m.weibo.cn/detail/4331511564696861?sudaref=login.sina.com.cn',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
         }


def headers():
    ti = time.strftime('%H:%M:%S', time.localtime())
    header = header1
    if 0 < int(ti[:2]) <= 8:
        header = header1
    elif 9 < int(ti[:2]) <= 16:
        header = header2
    elif 16 < int(ti[:2]) <= 24:
        header = header3
    return header



# 代理ip
ip_item = [
            {'ip': '220.180.50.14', 'port': 53281, 'type': 'HTTPS'},
            {'ip': '182.18.13.149', 'port': 53281, 'type': 'HTTPS'},
            {'ip': '222.186.20.28', 'port': 1080, 'type': 'HTTPS'},
            {'ip': '124.152.32.140', 'port': 53281, 'type': 'HTTPS'},
            {'ip': '59.44.247.194', 'port': 9797, 'type': 'HTTP'},
            {'ip': '222.74.61.98', 'port': 53281, 'type': 'HTTP'},
            {'ip': '61.145.182.27', 'port': 53281, 'type': 'HTTPS'},
            {'ip': '106.15.193.226', 'port': 3128, 'type': 'HTTPS'},
            {'ip': '58.17.125.215', 'port': 53281, 'type': 'HTTPS'},
            {'ip': '1.192.241.167', 'port': 9999, 'type': 'HTTP'},
            {'ip': '220.180.50.14', 'port': 53281, 'type': 'HTTPS'},
            {'ip': '14.118.130.213', 'port': 8081, 'type': 'HTTPS'},
            {'ip': '140.210.4.143', 'port': 53281, 'type': 'HTTPS'},
            {'ip': '1.196.160.90', 'port': 9999, 'type': 'HTTP'},
            {'ip': '116.85.46.113', 'port': 8080, 'type': 'HTTP'},
            {'ip': '58.247.127.145', 'port': 53281, 'type': 'HTTPS'},
            {'ip': '124.79.167.34', 'port': 9797, 'type': 'HTTPS'},
            {'ip': '221.7.255.168', 'port': 8080, 'type': 'HTTP'},
            {'ip': '101.251.216.103', 'port': 8080, 'type': 'HTTP'},
            {'ip': '58.56.108.237', 'port': 58690, 'type': 'HTTPS'},
            {'ip': '14.118.130.214', 'port': 8081, 'type': 'HTTP'},
            {'ip': '36.110.234.244', 'port': 80, 'type': 'HTTPS'},
            {'ip': '219.159.38.204', 'port': 56210, 'type': 'HTTP'},
            {'ip': '175.102.3.98', 'port': 8089, 'type': 'HTTP'},
            {'ip': '180.141.90.172', 'port': 53281, 'type': 'HTTPS'},
            {'ip': '119.1.97.192', 'port': 36751, 'type': 'HTTP'},
            {'ip': '219.159.38.208', 'port': 56210, 'type': 'HTTP'},
            {'ip': '202.204.121.126', 'port': 80, 'type': 'HTTP'},
            {'ip': '218.22.7.62', 'port': 53281, 'type': 'HTTPS'},
            {'ip': '121.69.46.178', 'port': 9000, 'type': 'HTTPS'},
            {'ip': '202.199.159.130', 'port': 40670, 'type': 'HTTP'},
            {'ip': '119.57.108.73', 'port': 53281, 'type': 'HTTPS'},
            {'ip': '120.79.7.88', 'port': 8118, 'type': 'HTTP'},
            {'ip': '113.140.1.82', 'port': 53281, 'type': 'HTTPS'},
            {'ip': '59.37.18.243', 'port': 3128, 'type': 'HTTPS'},
            {'ip': '58.250.23.210', 'port': 1080, 'type': 'HTTPS'},
            {'ip': '123.139.56.238', 'port': 9999, 'type': 'HTTPS'},
            {'ip': '113.200.214.164', 'port': 9999, 'type': 'HTTP'}]