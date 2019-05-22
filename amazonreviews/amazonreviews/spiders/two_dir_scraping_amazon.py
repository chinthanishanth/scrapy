# -*- coding: utf-8 -*-
import scrapy


class TwoDirScrapingAmazonSpider(scrapy.Spider):
    name = 'two_dir_scraping_amazon'
    allowed_domains = ['web']
    start_urls = ['http://web/']

    def parse(self, response):
        pass
