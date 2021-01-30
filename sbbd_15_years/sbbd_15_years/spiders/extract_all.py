# -*- coding: utf-8 -*-
import scrapy


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

    def parse(self, response):
        name = ""
        url = response.url
        year = self.get_year(response.url)
        data = []

        first = True
        for publishe_info, publishe_type in zip(response.css('li cite'),response.css('li div.box')):
            if first:
                first = False
                name = publishe_info.css(
                    'span.title::text').extract_first()

                continue

            paper_name = publishe_info.css(
                'span.title::text').extract_first()

            authors_name = publishe_info.css('span a span::text').extract()
            authors_url = publishe_info.css('span a::attr(href)').extract()
            author_data = [{name: url}
                           for name, url in zip(authors_name, authors_url)]

            
            
            category = publishe_type.css('img::attr(title)').extract_first()

            info_data = {
                'name': paper_name,
                'authors': author_data,
                'category': category
            }

            data.append(info_data)

        yield {
            'name': name,
            'url': url,
            'year': year,
            'data': data
        }

    def get_year(self, url):
        url = url[-10:-5]
        if url[0].isdigit():
            return url[:4]
        else:
            return url[1:]
