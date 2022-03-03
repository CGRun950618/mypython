# encoding= utf-8

#调度器-url管理器-网页下载-网页解析-数据存储

from DataOutput import DataOutput
from HtmlDownLoader import HtmlDownLoader
from HtmlParse import HtmlParse
from UrlManager import UrlManager

class SpilderMan(object):
    def __init__(self):
        self.manager=UrlManager()
        self.downloder=HtmlDownLoader()
        self.parse=HtmlParse()
        self.output=DataOutput()

    def crawl(self,root_url):
        #添加入口url
        self.manager.add_new_url(root_url)
        #判断url管理器中是否有新的url，同时抓了多少个url
        while(self.manager.has_new_url() and self.manager.old_url_size()<100):
            try:
                #从URL管理器中获取新的url
                new_url=self.manager.get_new_url()
                #Html下载器下载网页
                html=self.downloder.download(new_url)
                #抽取网页数据
                new_urls,data=self.parse.parse(new_url,html)
                #将抽取的url添加到url管理器中
                self.manager.add_new_urls(new_urls)
                #数据存储文件
                self.output.store_data(data)
                print ("已经抓取%s个链接"%self.manager.old_url_size())
            except Exception as e:
                print  ("crawl failed")
            #将数据存储器文件输出成指定格式
        self.output.output_html()

if __name__=="__main__":
    spider_man=SpilderMan()
    spider_man.crawl("https://www.baidu.com/")