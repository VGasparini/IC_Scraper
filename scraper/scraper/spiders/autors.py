# -*- coding: utf-8 -*-
import scrapy

class AutorsSpider(scrapy.Spider):
    name        = 'Autors Navigation'
    limit       = 50
    
    to_visit    = set()
    visited     = list()

    start_urls  = ['https://dblp.uni-trier.de/pers/hd/s/Schroeder:Rebeca']

    def parse(self, response):
        self.visited.append(response.url)

        
        yield { 'author' : response.css('head title::text').extract_first().replace('dblp: ','') }
        
        for coauthor in response.css('.person'):

            name = coauthor.css('a::text').extract_first()
            link = coauthor.css('a::attr("href")').extract_first()
            
            if link not in self.visited: 
                self.to_visit.add( link )

            yield { 'coauthor' : name, 'link' : link }
        
        if len(self.visited) < self.limit:
            visit_now = self.to_visit.pop()
            yield scrapy.Request(visit_now)