# -*- coding: utf-8 -*-
import scrapy


class SBBDAllDataSpider(scrapy.Spider):
    name = 'sbbd_all_data'
    allowed_domains = ['dblp.uni-trier.de/db/conf/sbbd']
    start_urls = ['http://dblp.uni-trier.de/db/conf/sbbd/']

    def parse(self, response):

        def get_conference_page_data():
            data = []
            for paper in response.css('li cite'):
                paper_name = paper.css(
                    'span.title::text').extract_first()

                authors_name = paper.css('span a span::text').extract()
                authors_url = paper.css('span a::attr(href)').extract()
                author_data = [{name: url}
                               for name, url in zip(authors_name, authors_url)]

                info_data = {
                    'name': paper_name,
                    'authors': author_data,
                }

                data.append(info_data)
            return data

        for conference in response.css('li cite'):
            conference_name = conference.css(
                'span.title::text').extract_first()
            conference_url = conference.css(
                'a.toc-link::attr(href)').extract_first()
            conference_year = conference.css('span::text').extract()[-1]

            editors_name = conference.css('span a span::text').extract()
            editors_url = conference.css('span a::attr(href)').extract()
            editor_data = [{name: url}
                           for name, url in zip(editors_name, editors_url)]

            yield scrapy.Request(
                conference_url,
                callback=self.parse
            )
            conference_page_data = get_conference_page_data()

            info_data = {
                'name': conference_name,
                'url': conference_url,
                'year': conference_year,
                'editors': editor_data,
                'papers': conference_page_data
            }

            yield info_data
