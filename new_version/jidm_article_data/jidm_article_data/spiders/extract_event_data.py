# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import requests
from time import sleep
from shortuuid import uuid


class ExtractProfileDataSpider(scrapy.Spider):
    name = 'extract_profile_data'
    allowed_domains = ['dblp.uni-trier.de']
    list_names = ['Rodrigo Gonçalves']

    start_urls = ['https://dblp.org/pid/94/5793']
    idx = 0

    def parse(self, response):
        def parse_event_page(url):
            tmp = requests.get(url).text
            sleep(10)
            try:
                return {
                    'nome': BeautifulSoup(tmp).find('ref').text,
                    'edicao': BeautifulSoup(tmp).find('h1').text,
                    'url': url
                }
            except:
                return {
                    'nome': None,
                    'edicao': None,
                    'url': url
                }

        data = []

        publish_path = response.css('li cite')
        type_path = response.css('li div.box img::attr(title)')
        publish_years = self.get_years(self.start_urls[self.idx] + '.xml')

        for article, article_type, year in zip(publish_path, type_path, publish_years):

            for idx, author in enumerate(article.css('span')):
                if 'this-person' in author.extract():
                    order = (idx+1)//2 + 1
                    break

            article_name = article.css('span.title::text').extract_first()

            try:
                event_url = article.css('a::attr(href)').extract(
                )[-1].split('#')[0].replace('.html', '.xml')
            except:
                event_url = None

            if event_url:
                data.append({
                    'id': uuid(),
                    'titulo': article_name,
                    'fonte': 'dblp',
                    'ordem': order,
                    'ano': year,
                    'tipo':  article_type.extract(),
                    'veiculo': parse_event_page(event_url)
                })

            else:
                data.append({
                    'id': uuid(),
                    'titulo': article_name,
                    'fonte': 'dblp',
                    'ordem': order,
                    'ano': year,
                    'tipo':  article_type.extract(),
                    'veiculo': None
                })

        yield {
            'nome': self.list_names[self.idx],
            'artigos': data
        }
        self.idx += 1

        if self.idx % 50 == 0:
            sleep(180)

    def get_years(self, url):
        tmp = requests.get(url).text
        years = [self.filter_year(y)
                 for y in BeautifulSoup(tmp).findAll('year')]
        return years

    def filter_year(self, year):
        return str(year).replace('<year>', '').replace('</year>', '')
