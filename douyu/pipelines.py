# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import uuid

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from douyu.settings import IMAGES_STORE
from pymongo import *


class DouyuPipeline(ImagesPipeline):
    def open_spider(self, spider):
        super(DouyuPipeline,self).open_spider(spider)
        client = MongoClient(host="127.0.0.1",port=27017)
        self.db = client.douyu

    def get_media_requests(self, item, info):
        yield scrapy.Request(
            url=item['room_src']
        )

    def item_completed(self, results, item, info):
        item['path'] = IMAGES_STORE + [x['url'] for ok, x in results if ok][0]
        print(item['path'])
        self.db.items.insert(dict(item))