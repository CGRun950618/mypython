# encoding= utf-8

# urllib3:requests 打开读取
        # {1.发起网络请求 2.操作cookie 3.添加headers 4.使用代理}
# urllib3:error 保护request抛出异常
# urllib3:parser 解析url
# urllib3:robotparser 解析robots.txt文件

# urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, context=None)
# cafile 为 CA 证书， capath 为 CA 证书的路径  context：ssl.SSLContext类型，用来指定 SSL 设置。

# urllib 侧重于 url 基本的请求构造
# urllib2侧重于 http 协议请求的处理，
# 而 urllib3是服务于升级的http 1.1标准，且拥有高效 http连接池管理及 http 代理服务的功能库

from urllib import request
# hupu=request.urlopen(url='https://bbs.hupu.com/get')
# print(hupu.read().decode())


# hupu=request.urlopen(url='https://bbs.hupu.com/posy',data=b'username=q123&password=123',timeout=0.1)
# print(hupu.read().decode())

#请求头
# hearders={
#     'Referer': 'https://bbs.hupu.com/',
#     'user':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
# }
# hupu=request.Request(url='https://bbs.hupu.com/get')
# hupu=request.urlopen(url=hupu)
# print(hupu.read().decode())

#操作cookie
# from http import cookiejar
# #创建cookie对象
# cookie=cookiejar.CookieJar()
# #创建cookie处理器
# cookies=request.HTTPCookieProcessor(cookie)
# #以它为参数，创建opener(cookies)
# opener=request.build_opener(cookies)
# res=opener.open('https://bbs.hupu.com/')
#
# print(cookies.cookiejar)

#设置代理
# url='http://httpbin.org/ip'
url='https://bbs.hupu.com/'
#代理地址
proxy={'http':'172.0.0.1:3128'}
#创建代理处理器
proxies=request.ProxyHandler(proxy)
#创建opener对象
opener=request.build_opener(proxies)

res=opener.open(url)
print(res.read().decode())