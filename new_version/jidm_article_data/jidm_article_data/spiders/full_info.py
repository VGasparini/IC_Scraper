# # -*- coding: utf-8 -*-
# import scrapy
# from bs4 import BeautifulSoup
# import requests
# from time import sleep


# class FullInfoSpider(scrapy.Spider):
#     pass
#     name = 'full_info'
#     allowed_domains = ['https://dblp.uni-trier.de/']
#     start_urls, list_names = [], []
#     idx = 0

#     with open('jidm_article_data/spiders/links') as f:
#         for line in f:
#             a, b = line.split(';')
#             list_names.append(a)
#             start_urls.append(b)

#     def parse(self, response):

#         url = response.url
#         years = self.get_years(url.replace('/hd/', '/xx/'))

#         data = []
#         for publishe_type, year in zip(response.css('li div.box img::attr(title)').extract(), years):
#             data.append({
#                 publishe_type: year,
#             })

#         self.idx += 1
#         yield {
#             'name': self.list_names[self.idx],
#             'publications': data
#         }

#         if self.idx % 150 == 0:
#             sleep(180)

#     def parse_author_page(self, response):
#         data = {}
#         publishes = []

#         name = ''
#         url = response.url

#         years = self.get_years(url.replace('/hd/', '/xx/'))

#         for publishe_info, publishe_type, year in zip(response.css('li cite'), response.css('li div.box img::attr(title)').extract(), years):
#             publishes.append({publishe_type: year})

#     def filter_year(self, year):
#         return str(year).replace('<year>', '').replace('</year>', '')

#     def get_years(self, url):
#         tmp = requests.get(url).text
#         years = [self.filter_year(y)
#                  for y in BeautifulSoup(tmp).findAll('year')]
#         return years
