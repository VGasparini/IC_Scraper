# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Coauthor(scrapy.Item):
    # define the fields for your item here like:
    coauthor = scrapy.Field()
    link     = scrapy.Field()

class Author(scrapy.Item):
    author   = scrapy.Field()
    link     = scrapy.Field()
    coauthor = list()

