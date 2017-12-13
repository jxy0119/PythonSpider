import requests
import re

iplist = [] ##初始化一个list用来存放我们获取到的IP
html = requests.get("http://www.66ip.cn/areaindex_1/1.html")##不解释咯
iplistn = re.findall(r'<tr>(.*?)</tr>', html.text, re.S)
for ip in iplistn:
    i = re.sub('</td><td>', ' ', ip)
    if i == ip or len(i) < 60:
        continue
    j = re.findall('<td>(.*?)</td>', i, re.S)[0]
    adr = j.split(' ')[0]
    port = j.split(' ')[1]
    adrr = adr + ':' + port
    print(adrr)
    iplist.append(adrr)
print(iplist)
 ##表示从html.text中获取所有r/><b中的内容，re.S的意思是包括匹配包括换行符，findall返回的是个list哦！
