# encoding= utf-8

import re
print(re.match('www','www.baidu.com').span())  #在起始位置匹配
print(re.match('ww.baidu.com','www.baidu.com'))


line='Cats are smarter than dogs'

serachObj=re.search(r'(.*)are(.*?).*',line,re.M|re.I)
#.*任意匹配除换行符\nr之外的任何单个或多个字符
#（.*?)“非贪婪”模式，只保存第一个匹配到子串

if serachObj:
    print("searchObj.group():", serachObj.group())
    print("searchObj.group(1):",serachObj.group(1))
else:
    print("Nothing found!!!")

#re.match尝试从字符串的起始位置匹配一个模式不是起始位置匹配放回none
#re.search扫描整个字符串返回第一成功的匹配
# re.match(pattern，匹配正则表达式
#           string, 要匹配的字符串
#           flags=0  标志位，控制正则表达式的匹配方式)

print(re.search('com','www.baidu.com'))
