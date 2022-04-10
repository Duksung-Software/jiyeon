BOT_NAME = 'G_market3'

SPIDER_MODULES = ['G_market3.spiders']
NEWSPIDER_MODULE = 'G_market3.spiders'

ROBOTSTXT_OBEY = False

LOG_FILE = 'G_market3.log'

FEED_EXPORT_ENCODING="utf-8-sig"

FEED_EXPORT_FIELDS = ['Name', 'Price', 'Deliver_Charge', 'URL']