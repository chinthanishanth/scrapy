# -*- coding: utf-8 -*-
import scrapy
from amazonreviews.items import AmazonreviewsItem

# exporting package list from  conda venv to req.txt
# conda list -e > req.txt
# creating a venv in  conda and installing packages from req.txt
# conda create -n new environment --file req.txt


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['web']
    start_urls = ['https://www.amazon.in/Apple-iPhone-X-64GB-Silver/product-reviews/B0711T2L8K/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews']
    def parse(self, response):

        item = AmazonreviewsItem()

        all_reviews_div = response.xpath(
            '//div[@data-hook="review"]')

        for review in range(0, len(all_reviews_div)):

            review_txt = all_reviews_div[review].xpath(
                './/*[@data-hook="review-body"]//text()').extract()

            rating = all_reviews_div[review].xpath(
                './/*[@data-hook="review-star-rating"]//text()').re('^[0-9]')

            item['review_txt'] = review_txt
            item['rating'] = rating
            yield item
