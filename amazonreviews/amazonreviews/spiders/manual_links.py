# -*- coding: utf-8 -*-
import scrapy
from amazonreviews.items import AmazonreviewsItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from urllib.parse import urljoin
from scrapy.http import Request, Response
import datetime
import socket
# exporting package list from  conda venv to req.txt
# conda list -e > req.txt
# creating a venv in  conda and installing packages from req.txt
# conda create -n new environment --file req.txt


class AmazonSpider(scrapy.Spider):
    name = 'links_manual'
    allowed_domains = ['https://www.amazon.in']
    start_urls = ['https://www.amazon.in/Apple-iPhone-X-64GB-Silver/product-reviews/B0711T2L8K/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews']

    def parse(self, response):
        '''
        This function extracts all the pagination links from the reviews of above amazon link
        '''

        # identify the next button
        next_link = response.xpath(
            '//*[@data-hook="pagination-bar"]//li[@class ="a-last"]//a/@href').extract_first()

        if next_link:
            next_link = response.urljoin(next_link)
            # next_link = urljoin('https://www.amazon.in', next_link)
            yield scrapy.Request(url=next_link, callback=self.parse, dont_filter=True)
