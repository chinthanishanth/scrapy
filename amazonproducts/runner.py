import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from amazonproducts.spiders import mobilephones


# to load current settings of the project navigate to the /home/nishanth/scrapy/amazonreviews (scrapy project directory)
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36',
    'AUTOTHROTTLE_ENABLED': 'True',
    'DOWNLOAD_DELAY': '3',
    'PROXY_POOL_ENABLED': 'True',
    'DOWNLOADER_MIDDLEWARES': {
        'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
        'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
    }
})
# process.crawl(amazon.AmazonSpider)
process.crawl(mobilephones.TwoDirScrapingAmazonSpider)

process.start()  # the script will block here until the crawling is finished
