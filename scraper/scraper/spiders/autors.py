# -*- coding: utf-8 -*-
import scrapy

class AutorsSpider(scrapy.Spider):
    name        = 'Autors Navigation'
    limit       = 3
    
    to_visit    = list()
    visited     = set()
    depth       = 0
    rank        = 0

    start_urls  = ['https://dblp.uni-trier.de/pers/hd/s/Schroeder:Rebeca']

    def parse(self, response):
        self.visited.add( response.url )

        data = {'author' : response.css('head title::text').extract_first().replace('dblp: ','') }

        data['coauthors'] = list()
        i = 0
        
        for coauthor in response.css('.person'):
            i += 1
            name = coauthor.css('a::text').extract_first()
            link = coauthor.css('a::attr("href")').extract_first()
            path = '//*[@id="coauthor-section"]/div/div/div[{}]/div[4]'.format(i)
            works = coauthor.xpath( path ).extract_first().count('#')
            
            if link not in self.visited: 
                self.to_visit.append( [link, self.rank] )

            tmp = {
                'name' : name,
                'link' : link,
                'works': works,
            }
            data['coauthors'].append( tmp )
            del tmp

        yield data

        self.rank += 1
        
        if self.to_visit[0][1] <= self.limit:
            visit_now = self.to_visit.pop(0)[0]
            yield scrapy.Request(visit_now)