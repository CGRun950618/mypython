# encoding= utf-8

import  re
from  urllib import parse
from  bs4  import  BeautifulSoup

class HtmlParse(object):
    def parse(self,page_url,html_cont):
        '''
        用于解析网页内容，抽取url和数据
        :param page_url:下载页面的url
        :param html_cont:下载页面的内容
        :return:返回url和数据
        '''
        if page_url is None or html_cont is None:
            return
        soup=BeautifulSoup(html_cont,'html.parse',from_encoding='utf-8')
        new_urls=self._get_new_urls(page_url,soup)
        new_data=self._get_new_data(page_url,soup)
        return new_urls,new_data

    def _get_new_urls(self, page_url, soup):
        '''
        抽取新的url集合
        :param page_url:下载页面的url
        :param soup: soup
        :return:返回新的url集合
        '''
        new_urls=set()  #抽取符合要求的a标记
        links=soup.find_all('a',herf=re.compile(r'/view/\d+\.htm'))
        for link in links:
            #提取href属性
            new_url=link['href']
            #拼接成完整网站
            new_full_url=parse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self,page_url,soup):
        '''
        抽取有效数据
        :param page_url:page_url
        :param soup:
        :return:
        '''
        data={}
        data['url']=page_url
        title=soup.find('dd',clas_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title']=title.get_text()
        summary=soup.find('div',class_='lemma-summary')
        #获取tag中包含所有文本内容，包括子孙tag
        data['summary']=summary.get_text()
        return data

