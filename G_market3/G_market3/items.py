import scrapy


class GMarket3Item(scrapy.Item):
    Name = scrapy.Field()
    Price = scrapy.Field()
    Delivery_Charge = scrapy.Field()
    URL = scrapy.Field()

