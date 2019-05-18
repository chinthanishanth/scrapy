# -*- coding: utf-8 -*-
import scrapy
from amazonreviews.items import AmazonreviewsItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from urllib.parse import urljoin
from scrapy.http import Request, Response
from scrapy.settings.default_settings import DOWNLOADER_MIDDLEWARES
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
        This function extracts all the reviews and pagination links from the reviews of above amazon link
        '''

        all_reviews_div = response.xpath('//div[@data-hook="review"]')

        for review in range(0, len(all_reviews_div)):

            i = ItemLoader(AmazonreviewsItem(), all_reviews_div[review])

            # required  items
            i.add_xpath(
                'review_txt', './/*[@data-hook="review-body"]//text()', Join())
            i.add_xpath(
                'rating', './/*[@data-hook="review-star-rating"]//text()', re='^[0-9]')

            # extra info fields
            i.add_value('url', response.url)
            i.add_value('project', self.settings.get('BOT_NAME'))
            i.add_value('spider', self.name)
            i.add_value('server', socket.gethostname())
            # using MapCompose for preprocessing items: converting datatime object to string
            i.add_value('date', datetime.date.today(),
                        MapCompose(lambda x: x.strftime('%Y/%m/%d')))
            i.add_value('ipaddr', response.headers.get('X-Proxymesh-Ip'))

            yield i.load_item()

    # identify the next button for looping review urls to extract more urls
        next_link = response.xpath(
            '//*[@data-hook="pagination-bar"]//li[@class ="a-last"]//a/@href').extract_first()

        if next_link:
            next_link = response.urljoin(next_link)
            # next_link = urljoin('https://www.amazon.in', next_link)
            yield scrapy.Request(url=next_link, callback=self.parse, dont_filter=True)
