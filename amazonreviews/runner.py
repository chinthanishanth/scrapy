import scrapy
from scrapy.crawler import CrawlerProcess

from amazonreviews.spiders import amazon, amazon_itemloader, manual_links, manual_links_items, manual_links_pagination_proxy

process = CrawlerProcess({
})

# process.crawl(amazon.AmazonSpider)
process.crawl(amazon_itemloader.AmazonSpider)
# process.crawl(manual_links.AmazonSpider)
# process.crawl(manual_links_items.AmazonSpider)
# process.crawl(manual_links_pagination_proxy.AmazonSpider)
process.start()  # the script will block here until the crawling is finished
