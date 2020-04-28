# -*- coding: utf-8 -*-
import scrapy


class SBBDCountSpider(scrapy.Spider):
    name = 'sbbd_count'
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
                  "https://dblp.uni-trier.de/db/conf/sbbd/sbbd2005.html",
                  "https://dblp.uni-trier.de/db/conf/sbbd/sbbd2004.html",
                  "https://dblp.uni-trier.de/db/conf/sbbd/sbbd2003.html",
                  "https://dblp.uni-trier.de/db/conf/sbbd/sbbd2002.html",
                  "https://dblp.uni-trier.de/db/conf/sbbd/sbbd2001.html",
                  "https://dblp.uni-trier.de/db/conf/sbbd/sbbd2000.html",
                  "https://dblp.uni-trier.de/db/conf/sbbd/sbbd1999.html"
                  ]
    category = {
        'c': 'proceeding-companion',
        's': 'short-paper',
        'p': 'poster'
    }

    def parse(self, response):
        first = True
        year = self.get_year(response.url)
        for paper in response.css('li cite'):
            if first:
                first = False
                continue

            authors_name = paper.css('span a span::text').extract()
            authors_url = paper.css('span a::attr(href)').extract()
            author_data = [{'name': name, 'url': url}
                           for name, url in zip(authors_name, authors_url)]
            category = self.classify(response.url)

            for author in author_data:
                info_data = {
                    'name': author['name'],
                    'url': author['url'],
                    'year': year,
                    'category': category
                }

                yield info_data

    def classify(self, url):
        if not url[-6].isdigit():
            return self.category.get(url[-6], 'full-paper')
        else:
            return 'full-paper'

    def get_year(self, url):
        url = url[-10:-5]
        if url[0].isdigit():
            return url[:4]
        else:
            return url[1:]
