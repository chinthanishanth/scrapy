import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from amazonproducts.spiders import mobilephones


# to load current settings of the project navigate to the /home/nishanth/scrapy/amazonreviews (scrapy project directory)
process = CrawlerProcess(get_project_settings())
# process.crawl(amazon.AmazonSpider)
process.crawl(mobilephones.TwoDirScrapingAmazonSpider)

process.start()  # the script will block here until the crawling is finished
