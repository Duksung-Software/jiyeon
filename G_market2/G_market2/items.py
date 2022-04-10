# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GMarket2Item(scrapy.Item):
    Name = scrapy.Field()
    Price = scrapy.Field()
    Delivery_Charge = scrapy.Field()
    URL = scrapy.Field()
    pass
