# -*- coding: utf-8 -*-
import scrapy


class SBBD_Crawler(scrapy.Spider):
    name = 'SBBD Crawler'
    start_urls = ['https://dblp.uni-trier.de/db/conf/sbbd/sbbd2005']
    to_visit = ['https://dblp.uni-trier.de/db/conf/sbbd/sbbd2006',
                'https://dblp.uni-trier.de/db/conf/sbbd/sbbd2007',
                'https://dblp.uni-trier.de/db/conf/sbbd/sbbd2008',
                'https://dblp.uni-trier.de/db/conf/sbbd/sbbd2009',
                'https://dblp.uni-trier.de/db/conf/sbbd/sbbd2010p',
                'https://dblp.uni-trier.de/db/conf/sbbd/sbbd2011s',
                'https://dblp.uni-trier.de/db/conf/sbbd/sbbd2012s',
                'https://dblp.uni-trier.de/db/conf/sbbd/sbbd2013',
                'https://dblp.uni-trier.de/db/conf/sbbd/sbbd2014',
                'https://dblp.uni-trier.de/db/conf/sbbd/sbbd2015',
                'https://dblp.uni-trier.de/db/conf/sbbd/sbbd2016',
                'https://dblp.uni-trier.de/db/conf/sbbd/sbbd2017',
                'https://dblp.uni-trier.de/db/conf/sbbd/sbbd2018',
                ]

    def parse(self, response):

        data = list()
        for publish in response.css('.data'):
            for author in publish.css('span'):
                name = author.css('a').css('span::text').extract_first()
                link = author.css('a::attr(href)').extract_first()
                if name != None:
                    data.append([name, link])

        atual_year = response.url[43:47]

        for i in data:
            yield {
                'name': i[0],
                'link': i[1],
                'year': atual_year
            }

        while len(self.to_visit) > 0:
            visit_now = self.to_visit[0]
            self.to_visit.pop(0)
            yield scrapy.Request(visit_now)

    def save(self, year, data):
        data.sort(key=lambda x: x[0])
        for inst in data:
            yield (inst[0], ': ', inst[1])
