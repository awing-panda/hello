# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from scrapy.conf import settings

class RrchespiderPipeline(object):
    def process_item(self, item, spider):
        return item

class MongodbRenrenchePipeline(object):

    def __init__(self):

        conn = pymongo.MongoClient(host=settings['MONGO_HOST'],
                                 port=settings['MONGO_PORT'])
        database = conn.renrenche
        self.collection = database['car_info']

    def process_item(self, item, spider):
        try:
            self.collection.update({'id': item['id']},
                                   {'$set': dict(item)},
                                   upsert=True)
        except:
            pass
        return item

