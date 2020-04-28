# -*- coding: utf-8 -*-
import scrapy


class SBBDOverviewSpider(scrapy.Spider):
    name = 'sbbd_overview_spider'
    allowed_domains = ['dblp.uni-trier.de/db/conf/sbbd']
    start_urls = ['http://dblp.uni-trier.de/db/conf/sbbd/']

    def parse(self, response):
        for conference in response.css('li cite'):
            conference_name = conference.css(
                'span.title::text').extract_first()
            conference_url = conference.css(
                'a.toc-link::attr(href)').extract_first()
            conference_year = conference.css(
                'span::text').extract()[-1]

            editors_name = conference.css('span a span::text').extract()
            editors_url = conference.css('span a::attr(href)').extract()
            editor_data = [{name: url}
                           for name, url in zip(editors_name, editors_url)]

            info_data = {
                'name': conference_name,
                'url': conference_url,
                'year': conference_year,
                'editors': editor_data,
            }

            yield info_data
