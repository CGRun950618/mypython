
import os
import random
import requests
#下载图片脚本用到的库

path2 = r'D://爬虫路径'
os.mkdir(path2 + './'+"test")
#以上两行即在d盘tu目录下创建名称为test的文件夹

c = "http://img1.cache.netease.com/cnews/img/logo2013/s/news.png"
#图片地址

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
headers = {'user-agent': user_agent}
#头信息，后面请求图片地址的时候需要带上，否则容易禁止访问

print("loading"+" " +c)

pic_name = random.randint(0,100)#图片名称随机命令

r = requests.get(c,stream=True,headers=headers)#请求图片地址，注意”r“

with open(path2 + './'+"test" +'./'+str(pic_name) +'.jpg', 'wb') as fd:
    for chunk in r.iter_content():
        fd.write(chunk)
#下载脚本，实际就是把图片保存到D盘tu目录test文件夹pic_name文件中