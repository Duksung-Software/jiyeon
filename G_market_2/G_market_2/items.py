
import scrapy


class GMarket2Item(scrapy.Item):
    Array = scrapy.Field()
    Item = scrapy.Field()
    Price = scrapy.Field()
    URL = scrapy.Field()

