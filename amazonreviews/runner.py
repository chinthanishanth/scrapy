import scrapy
from scrapy.crawler import CrawlerProcess

from amazonreviews.spiders import amazon

process = CrawlerProcess({
})

process.crawl(amazon.AmazonSpider)
process.start()  # the script will block here until the crawling is finished
