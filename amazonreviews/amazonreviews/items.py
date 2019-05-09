# -*- coding: utf-8 -*-

from scrapy.item import Field, Item


class AmazonreviewsItem(Item):

    # required  items
    review_txt = Field()
    rating = Field()

    # extra info fields
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()
