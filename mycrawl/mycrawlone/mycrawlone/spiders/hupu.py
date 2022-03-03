# encoding= utf-8
import scrapy



class BookSpider(scrapy.Spider):
    name="hupu"
    # allowed_domains  start_urls

    allowed_domain=['bbs.hupu.com']
    start_urls=['https://bbs.hupu.com/4860/']

    # def parse(self, response):
    #     titles=response.xpath('//html/head/title/meta')
    #     print(titles)

    def parse(self, response):
        titles=response.xpath('//@class')
        print(titles)
