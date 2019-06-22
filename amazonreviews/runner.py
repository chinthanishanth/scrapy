import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from amazonreviews.spiders import amazon, amazon_itemloader, manual_links, manual_links_items, manual_links_pagination_proxy

# to load current settings of the project navigate to the /home/nishanth/scrapy/amazonreviews (scrapy project directory)
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36',
    'ITEM_PIPELINES': {
        'amazonreviews.pipelines.AmazonreviewsPipeline': 300,
    },
    'ROBOTSTXT_OBEY': 'True',
    'BOT_NAME': 'amazonreviews'
})

# process.crawl(amazon.AmazonSpider)
# process.crawl(amazon_itemloader.AmazonSpider)
# process.crawl(manual_links.AmazonSpider)
process.crawl(manual_links_items.AmazonSpider)
# process.crawl(manual_links_pagination_proxy.AmazonSpider)
process.start()  # the script will block here until the crawling is finished
