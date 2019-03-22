# -*-coding:utf-8-*-

import re

'''
‘.’用于匹配除换行符（\n）之外的所有字符。
‘^’用于匹配字符串的开始，即行首。
‘$’用于匹配字符串的末尾（末尾如果有换行符\n，就匹配\n前面的那个字符），即行尾。
‘*’用于将前面的模式匹配0次或多次（贪婪模式，即尽可能多的匹配）
‘+’用于将前面的模式匹配1次或多次（贪婪模式）
‘？’用于将前面的模式匹配0次或1次（贪婪模式）
‘*？，+？，？？’即上面三种特殊字符的非贪婪模式（尽可能少的匹配）。
‘{m,n}’用于将前面的模式匹配m次到n次（贪婪模式），即最小匹配m次，最大匹配n次。
‘{m,n}？’即上面‘{m,n}’的非贪婪版本。
‘\\’：'\'是转义字符，在特殊字符前面加上\，特殊字符就失去了其所代表的含义，比如\+就仅仅代表加号+本身。
‘[]’用于标示一组字符，如果^是第一个字符，则标示的是一个补集。比如[0-9]表示所有的数字，[^0-9]表示除了数字外的字符。
‘[...]’用来表示一组字符，单独列出：[amk] 匹配 'a'，'m' 或 'k'
‘|’比如A|B用于匹配A或B。
‘(...)’用于匹配括号中的模式，可以在字符串中检索或匹配我们所需要的内容。
'''

'''
\A：表示从字符串的开始处匹配
\Z：表示从字符串的结束处匹配，如果存在换行，只匹配到换行前的结束字符串。
\b：匹配一个单词边界，也就是指单词和空格间的位置。例如， 'py\b' 可以匹配"python" 中的 'py'，但不能匹配 "openpyxl" 中的 'py'。
\B：匹配非单词边界。 'py\b' 可以匹配"openpyxl" 中的 'py'，但不能匹配"python" 中的 'py'。
\d：匹配任意数字，等价于 [0-9]。
\D：匹配任意非数字字符，等价于 [^\d]。
\s：匹配任意空白字符，等价于 [\t\n\r\f]。
\S：匹配任意非空白字符，等价于 [^\s]。
\w：匹配任意字母数字及下划线，等价于[a-zA-Z0-9_]。  \w能不能匹配汉字要视你的操作系统和你的应用环境而定
\W：匹配任意非字母数字及下划线，等价于[^\w]
\\：匹配原义的反斜杠\。
'''

'''
修饰符	描述
re.I	使匹配对大小写不敏感
re.L	做本地化识别（locale-aware）匹配
re.M	多行匹配，影响 ^ 和 $
re.S	使 . 匹配包括换行在内的所有字符
re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解
'''

l1 = re.split(r'[\s\,/\%\\]+','a/, b,c\,   r, %%, d')    # 切分字符串，结果为list
# print(l1)

l2 = re.match(r'^(\d+?)(0*)$','1230540000')    # 正则默认是贪婪匹配，加个？号，去掉贪婪匹配，分组匹配
# print(ll2.groups())
# print(ll2.group(2))

'''
match与search都只匹配符合条件的一个结果（非贪婪），match只匹配字符串的开始位置，search既可以匹配首位置，也可匹配非首位置
'''
l3 = re.search('[Pp]ython','book door Python son python')
# print(l3.group())


s = '610524199306256037'
res = re.search('(?P<province>\d{2})(?P<city>\d{2})(?P<part>\d{2})(?P<born_year>\d{4})(?P<birthday>\d{4})(?P<police_code>\d{2})(?P<sex>\d{1})(?P<check_code>\d{1})',s)
# print(res.groupdict())


'''
match与search只匹配一次，findall是匹配所有、结果是列表的形式
'''
s1 = re.findall('\d+','s46dsf45f6f放假你发759等等')     # 提取字符串中的数字 46 45 6 759
# print(s1)


pa = re.compile(r'\d+')   # 查找数字
r1 = pa.findall('runoob 123 google 456')
r2 = pa.findall('run88oob123google456', 0, 10)   # 表示从起始位置开始的前10个字符
# print(r1)
# print(r2)


'''
对于字符串abcgabc
贪婪模式– a.*c –得到的答案为：abcgabc
懒惰模式– a.*?c –得到的答案为：abc,abc
'''
l4 = 'abcgabcxabc'
p0 = re.findall('a.*c',l4)      # 结果：['abcgabcxabc']
# p0 = re.findall('a.*?c',l4)     # 结果：['abc', 'abc', 'abc']
# print(p0)


# 去掉html标签
'''
*用于将前面的模式匹配零次或多次（贪婪模式）
+用于将前面的模式匹配1次或多次（贪婪模式）
?用于将前面的模式匹配0次或1次（贪婪模式）
有括号时只能匹配到括号中的内容
'''
s2 = r"回复<a href='https://m.weibo.cn/n/红色在舞蹈'>@红色在舞蹈</a>:是的，我女儿一岁半也不会说，现在话痨"
p1 = re.compile(r'</?\w+[^>]*>')
# print(p1.sub('',s2))


# 找寻一个字符串在整个字符串中出现的次数|字符串本身就是正则表达式
s3 = re.findall('python','dsds python python python fdfd python python ddpython')
# print(len(s3))


# 匹配ip地址的正则
s4 = "'ip': '222.74.61.98', 'port': 53281, 'type': 'HTTP''ip': '58.249.55.222', 'port': 9797, 'type': 'HTTP''ip': '61.145.182.27', 'port': 53281, 'type': 'HTTPS'}"
p2 = re.findall('\d+\.\d+\.\d+\.\d+',s4)
# print(p2)


'''
可以使用非捕获元字符 ?:、?= 或 ?! 来重写捕获，忽略对相关匹配的保存
'''
s5 ='''2019-02-13 18:31:07","https://www.douyin.com/aweme/v1/aweme/post/?user_id=95748601983&count=21&max_cursor=0&aid=1128&dytk=b4769e42c4fe4e8db3a6e703bbd92818&_signature=AGiwhQAAXBD.l096i95fsABosJ#0","6654160086253997324","95748601983","http://p9-dy.bytecdn.cn/aweme/720x720/c7cd000b9a3b14b85513.jpeg","贝知美孕育知识分享","B020520","","广东·广州","金牛座","4","11.2w","70.4w","https://p1.pstatp.com/large/1989b000399174297bfd7.jpg","春节不出错，习俗知多点！","434","1280","720","https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300fb00000bhcicik7u4t5h87blu60&line=0",
"2019-02-13 18:31:08","https://www.douyin.com/aweme/v1/aweme/post/?user_id=75748601983&count=21&max_cursor=0&aid=1128&dytk=b4769e42c4fe4e8db3a6e703bbd92818&_signature=AGiwhQAAXBD.l096i95fsABosJ#9","6639576492990795022","95748601983","http://p9-dy.bytecdn.cn/aweme/720x720/c7cd000b9a3b14b85513.jpeg","贝知美孕育知识分享","B020520","","广东·广州","金牛座","4","11.2w","70.4w","https://p3.pstatp.com/large/15235000bdd0a33f0674b.jpg","孕期不要做这五件事！后悔就晚了～#孕孕孕 #孕期 #孕日常孕孕 @抖音小助手 @贝知美育儿百科","31","1280","720","https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200fe10000bgi877vijqtconlu6ae0&line=0",
"2019-02-13 18:31:07","https://www.douyin.com/aweme/v1/aweme/post/?user_id=89748601983&count=21&max_cursor=0&aid=1128&dytk=b4769e42c4fe4e8db3a6e703bbd92818&_signature=AGiwhQAAXBD.l096i95fsABosJ#1","6653709565537897732","95748601983","http://p9-dy.bytecdn.cn/aweme/720x720/c7cd000b9a3b14b85513.jpeg","贝知美孕育知识分享","B020520","","广东·广州","金牛座","4","11.2w","70.4w","https://p1.pstatp.com/large/19647000a168559719788.jpg","各地食俗，春节必吃，寓意你都知道吗？","2","1280","720","https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f1f0000bhbuo1v82ijg229t9p90&line=0",
"2019-02-13 18:31:08","https://www.douyin.com/aweme/v1/aweme/post/?user_id=95748601983&count=21&max_cursor=0&aid=1128&dytk=b4769e42c4fe4e8db3a6e703bbd92818&_signature=AGiwhQAAXBD.l096i95fsABosJ#2","6652903682843200782","95748601983","http://p9-dy.bytecdn.cn/aweme/720x720/c7cd000b9a3b14b85513.jpeg","贝知美孕育知识分享","B020520","","广东·广州","金牛座","4","11.2w","70.4w","https://p1.pstatp.com/large/190d3000d5a0edd7a8ebb.jpg","过年期间，给宝宝喂食要注意！#抖音小助手","9","1280","720","https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f6f0000bhah69ignbhf555n686g&line=0",
"2019-02-13 18:31:08","https://www.douyin.com/aweme/v1/aweme/post/?user_id=ee748601983&count=21&max_cursor=0&aid=1128&dytk=b4769e42c4fe4e8db3a6e703bbd92818&_signature=AGiwhQAAXBD.l096i95fsABosJ#3","6652520235960241416","95748601983","http://p9-dy.bytecdn.cn/aweme/720x720/c7cd000b9a3b14b85513.jpeg","贝知美孕育知识分享","B020520","","广东·广州","金牛座","4","11.2w","70.4w","https://p1.pstatp.com/large/192ee0002d3cf3ad080ad.jpg","新春将至，孕妈要注意什么？","1789","1280","720","https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f550000bh9oq6o697avc1jvais0&line=0",
"2019-02-13 18:31:08","https://www.douyin.com/aweme/v1/aweme/post/?user_id=95748521983&count=21&max_cursor=0&aid=1128&dytk=b4769e42c4fe4e8db3a6e703bbd92818&_signature=AGiwhQAAXBD.l096i95fsABosJ#4","6652272520554712333","95748601983","http://p9-dy.bytecdn.cn/aweme/720x720/c7cd000b9a3b14b85513.jpeg","贝知美孕育知识分享","B020520","","广东·广州","金牛座","4","11.2w","70.4w","https://p1.pstatp.com/large/16f8d000884bf5eb0365c.jpg","今年，你回家过年吗？#我们的新年心同步 #春运看我瞬移回家 #我的温暖回家路 #抖音小助手","8","720","1280","https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300fa70000bh93f78e8b7kstrv18m0&line=0",
"2019-02-13 18:31:08","https://www.douyin.com/aweme/v1/aweme/post/?user_id=95748601983&count=21&max_cursor=0&aid=1128&dytk=b4769e42c4fe4e8db3a6e703bbd92818&_signature=AGiwhQAAXBD.l096i95fsABosJ#5","6652268970734996750","95748601983","http://p9-dy.bytecdn.cn/aweme/720x720/c7cd000b9a3b14b85513.jpeg","贝知美孕育知识分享","B020520","","广东·广州","金牛座","4","11.2w","70.4w","https://p3.pstatp.com/large/18f79000c9daa6f6a29d7.jpg","回家过年，幸福从来不远，你今年回家过年吗？#带团圆回家 #拜个抖音年 #抖音小助手","7","720","1280","https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300fc40000bh8qh9ju89igegotk68g&line=0",
"2019-02-13 18:31:08","https://www.douyin.com/aweme/v1/aweme/post/?user_id=95748601983&count=21&max_cursor=0&aid=1128&dytk=b4769e42c4fe4e8db3a6e703bbd92818&_signature=AGiwhQAAXBD.l096i95fsABosJ#6","6639889099467541773","95748601983","http://p9-dy.bytecdn.cn/aweme/720x720/c7cd000b9a3b14b85513.jpeg","贝知美孕育知识分享","B020520","","广东·广州","金牛座","4","11.2w","70.4w","https://p1.pstatp.com/large/151be000cc6a0373f5662.jpg","宝宝的奶瓶，你用对了吗@贝知美育儿百科 @贝知美纸尿裤","132","1280","720","https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f870000bgipvr4m7fi13clf8efg&line=0",
"2019-02-13 18:31:08","https://www.douyin.com/aweme/v1/aweme/post/?user_id=95748601983&count=21&max_cursor=0&aid=1128&dytk=b4769e42c4fe4e8db3a6e703bbd92818&_signature=AGiwhQAAXBD.l096i95fsABosJ#7","6639844811425713416","95748601983","http://p9-dy.bytecdn.cn/aweme/720x720/c7cd000b9a3b14b85513.jpeg","贝知美孕育知识分享","B020520","","广东·广州","金牛座","4","11.2w","70.4w","https://p3.pstatp.com/large/1523c00056e6353da70d0.jpg","男生成为丈夫前，应该要知道的事！@贝知美纸尿裤 @贝知美育儿百科","216","1280","720","https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200fe10000bginfaqmac2v78hfapl0&line=0",
"2019-02-13 18:31:08","https://www.douyin.com/aweme/v1/aweme/post/?user_id=95748601983&count=21&max_cursor=0&aid=1128&dytk=b4769e42c4fe4e8db3a6e703bbd92818&_signature=AGiwhQAAXBD.l096i95fsABosJ#8","6639579542782479624","95748601983","http://p9-dy.bytecdn.cn/aweme/720x720/c7cd000b9a3b14b85513.jpeg","贝知美孕育知识分享","B020520","","广东·广州","金牛座","4","11.2w","70.4w","https://p1.pstatp.com/large/154a800007f499e507365.jpg","冬天给孩子穿太多不可取，要懂得的“穿衣公式”！@贝知美育儿百科 @贝知美纸尿裤","2054","1280","720","https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200fda0000bgi8cp5d2r668n33t0l0&line=0",
"2019-02-13 18:31:08","https://www.douyin.com/aweme/v1/aweme/post/?user_id=95748601983&count=21&max_cursor=0&aid=1128&dytk=b4769e42c4fe4e8db3a6e703bbd92818&_signature=AGiwhQAAXBD.l096i95fsABosJ#9","6639576492990795022","95748601983","http://p9-dy.bytecdn.cn/aweme/720x720/c7cd000b9a3b14b85513.jpeg","贝知美孕育知识分享","B020520","","广东·广州","金牛座","4","11.2w","70.4w","https://p3.pstatp.com/large/15235000bdd0a33f0674b.jpg","孕期不要做这五件事！后悔就晚了～#孕孕孕 #孕期 #孕日常孕孕 @抖音小助手 @贝知美育儿百科","31","1280","720","https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200fe10000bgi877vijqtconlu6ae0&line=0",
'''
# p3 = re.findall(r'https?://[^, "]*?\.(?:jpg|png|jpeg)',s5)
# p3 = re.findall('\d{19}',s5)
# p3 = re.findall('http',s5)
# p3 = re.findall('https?://[^"| ]*?(?=")',s5)     # ?="表示匹配"但结果不包含"      基于对目标字符串的观察
p3 = re.findall('https?://[^" ]*?(?:line=0)',s5)     # ?:"表示匹配"且结果包含"    基于对目标字符串的观察
# p3 = re.findall('(?!user_id=)\d{11}(?=&)',s5)     # 在前面匹配但结果不包含用?!    在后面匹配但结果不包含用?=
# for i in p3:
#     print(i)


# 利用\b提取以空格分开的单词
s6 ='site sea sue sweet  seeu case se sse ssuee losest'
p4 = re.findall(r'\bs\S*?e\b',s6)     # 以s开头以e结尾的单词
# p4 = re.findall(r'\bc\S*',s6)      # 以s开头的单词
# p4 = re.findall(r'\S*?t\b',s6)      # 以t结尾的单词
# p4 = re.findall(r'\S*?u\S*',s6)      # 包含u的单词
# print(p4)


# 准确识别身份证(identity card)号
s7 = '''513436200004444
姓名	身份证号
燕善	513436200003196寿蕊	513436200004196211戚雪	513436200006197葛健发dfsdf	513436200007199615袁龙凡ssd	513436200009196 fffff   thrthrt854516548546546
845646546513274123hth    ttgg232135315555656565thrthhgthgbg41213132684572457Xgbgnhrth柏纯林	
51343620000319825X'''
p5 = re.findall('\D\d{15}(?=\D)|\D\d{18}(?=\D)|\D\d{17}X',s7)     # 身份证最后一位X是大写 表示10  X罗马数字
# for i in p5:
#     ID_card_num = i[1:]
#     print(ID_card_num,' '*2,str(len(ID_card_num))+"位")


# 检查电子邮箱地址(是否合法)
s8 = '''736410328@qq.com  dfdfdf lym_6017@163.com3  sdawdwefw wang1984930@163.com5   niulangzhinv@sina.com2   lym_6017@ce.cn 
ssdfdfd    dfsf f efdf   lym_6017@china.com.cn1
'''
p6 = re.findall('\w+@\w+\.(?:com\.cn|com|cn)',s8)
# for i in p6:
#     print(i)

'''
flags参数的学习
'''
# re.M 将所有行的尾字母或者首部输出
S3 = '''I am girl
        you are boy
        we are friends
        you are my friend
        '''                   #定义初始字符串
# print(re.findall(r"\w+$",S3,re.M))   #输出S3的每行最后一个字符串

# re.I 忽略大小写    ignore
S1 = 'con'   #定义字符串i1
S2 = 'www.xiao.con,cOn,coN'
# print(re.search('CoN','www.xiao.con').group())  #区分大小写的子组输出,报有错
# print(re.findall(S1,S2,re.I))  #不区分大小写的子组输出

# re.S匹配包括换行在内的所有字符
s11 = '''jduedhhelloworld
11630
passgrthgdg
hello555444
world
passsdfs
'''         #初始字符串，有换行所以用三引号
b = re.findall('hello(.*?)pass',s11)
c = re.findall('hello(.*?)pass',s11,re.S)  #包含换行
# print('b is',b)  #输出B匹配的结果
# print('c is',c)   #输出C，包行匹配输出的结果

t1 = """/*this is a 
     multiline comment */"""
comm = re.compile(r'/\*(.*?)\*/', flags=re.DOTALL)       # re.DOTALL相当于re.S 可以互相替换
# print(comm.findall(t1))

# ^ 和 $ 的用法
t2 = 'jhdbd2123568555dds7'
c1 = re.findall('^jhd',t2)     # ^只判断字符串是否以某几个字符开始，不是的话返回空列表，可用来做判断
# co = re.findall('s7$',t2)      # $只判断字符串是否以某几个字符结束，不是的话返回空列表，可用来做判断
# print(co)


t3 = 'd12df5d5d554g6rfg3'
c2 = re.findall('\D+',t3)
# print(c2)

t4 = 'a5DKf~!……￥@#$%^&*()_+|":?/><'
# c3 = re.findall('\w',t4)      # \w 匹配字母数字下划线，不包含特殊字符
c3 = re.findall('\W',t4)
print(c3)


