# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import requests


class SBBDConferenceSpider(scrapy.Spider):
    name = 'sbbd_conference'
    allowed_domains = ['dblp.uni-trier.de/db/conf/sbbd']
    start_urls = ["https://dblp.uni-trier.de/db/conf/sbbd/sbbd2019.html",
                "https://dblp.uni-trier.de/db/conf/sbbd/sbbd2018.html",
                "https://dblp.uni-trier.de/db/conf/sbbd/sbbd2018c.html",
                "https://dblp.uni-trier.de/db/conf/sbbd/sbbd2017.html",
                "https://dblp.uni-trier.de/db/conf/sbbd/sbbd2017s.html",
                "https://dblp.uni-trier.de/db/conf/sbbd/sbbd2016.html",
                "https://dblp.uni-trier.de/db/conf/sbbd/sbbd2015.html",
                "https://dblp.uni-trier.de/db/conf/sbbd/sbbd2015s.html",
                "https://dblp.uni-trier.de/db/conf/sbbd/sbbd2014.html",
                "https://dblp.uni-trier.de/db/conf/sbbd/sbbd2013s.html",
                "https://dblp.uni-trier.de/db/conf/sbbd/sbbd2012s.html",
                "https://dblp.uni-trier.de/db/conf/sbbd/sbbd2011s.html",
                "https://dblp.uni-trier.de/db/conf/sbbd/sbbd2010p.html",
                "https://dblp.uni-trier.de/db/conf/sbbd/sbbd2009.html",
                "https://dblp.uni-trier.de/db/conf/sbbd/sbbd2008.html",
                "https://dblp.uni-trier.de/db/conf/sbbd/sbbd2007.html",
                "https://dblp.uni-trier.de/db/conf/sbbd/sbbd2006.html",
                "https://dblp.uni-trier.de/db/conf/sbbd/sbbd2005.html"
                ]
    links_to_visit = set()

    def get_year(self, url):
        url = url[-10:-5]
        if url[0].isdigit():
            return url[:4]
        else:
            return url[1:]

    def parse(self, response):
        first = True
        for publishe_info in response.css('li cite'):
            if first:
                first = False
                continue

            authors_name = publishe_info.css('span a span::text').extract()
            authors_url = publishe_info.css('span a::attr(href)').extract()

            for name,url in zip(authors_name,authors_url):
                i = tuple([name,url])
                if i not in self.links_to_visit:
                    self.links_to_visit.add(i)
        
        for name,url in self.links_to_visit:
            yield {
                name:url,
            }

    def parse_author_page(self, response):
        data = {}
        publishes = []

        name = ''
        url = response.url

        years = self.get_years(url.replace('/hd/','/xx/'))

        for publishe_info, publishe_type, year in zip(response.css('li cite'),response.css('li div.box img::attr(title)').extract(), years):
            publishes.append({ publishe_type : year })

    def filter_year(self, year):
        return year.replace('<year>','').replace('</year>','')

    def get_years(self, url):
        tmp = requests.get(url)
        years = map(self.filter_year,tmp.findAll('year'))
        return years
