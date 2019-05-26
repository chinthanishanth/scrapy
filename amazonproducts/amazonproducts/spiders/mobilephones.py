# -*- coding: utf-8 -*-
import scrapy
from amazonproducts.items import AmazonproductsItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from urllib.parse import urljoin


class TwoDirScrapingAmazonSpider(scrapy.Spider):
    name = 'mobilephones'
    allowed_domains = ['web']
    start_urls = [
        'https://www.amazon.in/s?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cn%3A1389432031']

    page_number = 2

    def parse(self, response):
        """
        This function extracts all the product urls list in a page and product details and follows
        pagination to extract more product urls
        """

        div_containing_mobile_links = response.xpath(
            '//*[contains(@id,"result_") or @data-asin]')

        extracted_mobile_links = div_containing_mobile_links.xpath(
            './/*[@class = "a-link-normal a-text-normal"]/@href').extract()

        # removing duplicated links in the list
        extracted_mobile_links_no_dup = list(set(extracted_mobile_links))

        for link in extracted_mobile_links_no_dup:
            yield scrapy.Request(url=link, callback=self.parse_items, dont_filter=True)

        # follow pagination links and collect more mobile phone links
        next_page = 'https://www.amazon.in/s?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cn%3A1389432031&page=' + \
            str(TwoDirScrapingAmazonSpider.page_number)
        TwoDirScrapingAmazonSpider.page_number = TwoDirScrapingAmazonSpider.page_number + 1
        yield scrapy.Request(url=next_page, callback=self.parse, dont_filter=True)

    def parse_items(self, response):

        i = ItemLoader(item=AmazonproductsItem(), response=response)

        # i.add_xpath('link', response.url)
        i.add_xpath('product_title',
                    '//*[@id="title"]//text()', MapCompose(lambda x: x.strip()))
        i.add_xpath(
            'price', '//*[@id="priceblock_dealprice" or @id = "priceblock_ourprice"]//text()', MapCompose(lambda x: ''.join(x).replace(u'\xa0', u'').replace(',', '').strip()))
        i.add_xpath('product_details',
                    '//*[@id="feature-bullets"]//text()', MapCompose(lambda x: x.strip()))

        yield i.load_item()
