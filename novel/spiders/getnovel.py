# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from bs4 import BeautifulSoup
from novel.items import NovelItem
import re

class GetnovelSpider(Spider):
    name = 'getnovel'
    allowed_domains = ['www.x23us.com']
    start_urls = ['http://www.x23us.com/']
    bash_url = 'http://www.x23us.com/class/'
    bashurl = '.html'

    def start_requests(self):
        for i in range(1, 11):

            url = self.bash_url + str(i) + '_1'+self.bashurl
            y = Request(url, callback=self.parse)
            print(y)
            yield y
        yield Request('http://www.x23us.com/quanben/1', callback=self.parse)

    def parse(self, response):
        z = response.request.headers
        print(z)
        max_num = BeautifulSoup(response.text, 'lxml').find('div', class_='pagelink').find_all('a')[-1].get_text()
        bashurl = str(response.url)[:-7]
        for num in range(1, int(max_num) + 1):
            url = bashurl + '_' + str(num) + self.bashurl
            yield Request(url, self.get_name)
        # print(response.text)

    def get_name(self, response):
        tds = BeautifulSoup(response.text, 'lxml').find_all('tr', bgcolor='#FFFFFF')
        for td in tds:
            novelname = td.find_all('a')[1].get_text()
            novelurl = td.find('a')['href']
            yield Request(novelurl,callback=self.get_content, meta={'name': novelname, 'url': novelurl})

        #print(response.text)

    def get_content(self, response):
        item = NovelItem()
        item['name'] = str(response.meta['name'])
        item['url'] = str(response.meta['url'])
        category = BeautifulSoup(response.text, 'lxml').find('table').find('a').get_text()
        author = BeautifulSoup(response.text, 'lxml').find('table').find_all('td')[1].get_text()
        bash_url = BeautifulSoup(response.text, 'lxml').find('p', class_='btnlinks').find('a', class_='read')['href']
        name_id = str(bash_url)[-6:-1]



        print(response.text)
