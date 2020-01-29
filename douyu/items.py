# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    room_id = scrapy.Field()
    room_name = scrapy.Field()
    room_src = scrapy.Field()
    nickname = scrapy.Field()
    path = scrapy.Field()