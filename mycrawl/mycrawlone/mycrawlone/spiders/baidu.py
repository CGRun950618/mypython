# encoding= utf-8

import scrapy



class BookSpider(scrapy.Spider):
    name="baidu"
    # allowed_domains  start_urls

    allowed_domain=['www.baidu.com']
    start_urls=['https://www.baidu.com/']

    def parse(self, response):
        titles=response.xpath('//html/head/title')
        print(titles)