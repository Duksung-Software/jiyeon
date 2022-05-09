
BOT_NAME = 'G_market_2'

SPIDER_MODULES = ['G_market_2.spiders']
NEWSPIDER_MODULE = 'G_market_2.spiders'


ROBOTSTXT_OBEY = False
LOG_FILE = 'G_Market_2.log'

FEED_EXPORT_ENCODING = 'utf-8-sig'
FEED_EXPORT_FIELDS = ['Keyword', 'Item', 'Price', 'URL']
