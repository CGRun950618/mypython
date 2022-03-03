# encoding= utf-8
#网页下载器

import requests

class HtmlDownLoader(object):
    def download(self,url):
        if url is None:
            return None
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
        headers={'user-agent':user_agent}
        r=requests.get(url,headers=headers)
        if r.status_code==200:
            r.encoding='utf-8'
            return r.text
        return None
