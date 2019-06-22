# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo


class AmazonreviewsPipeline(object):

    def __init__(self):
        self.conn = pymongo.MongoClient('172.18.0.4', 27017)
        db = self.conn['amazonreviews']
        self.collection = db['amazonreviews_tbl']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
