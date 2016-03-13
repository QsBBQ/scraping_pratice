# Scrapy settings for hackernews project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'hackernews'

SPIDER_MODULES = ['hackernews.spiders']
NEWSPIDER_MODULE = 'hackernews.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'hackernews (+http://www.yourdomain.com)'