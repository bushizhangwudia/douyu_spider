# -*- coding: utf-8 -*-
import json
from pprint import pprint
from douyu.items import DouyuItem
import jsonpath
import scrapy


class DySpider(scrapy.Spider):
    name = 'dy'
    allowed_domains = ['douyucdn.cn']
    base_url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset={}'
    start_urls = []
    for num in range(0,1020,20):
        start_urls.append(base_url.format(num))

    def parse(self, response):
        res = json.loads(response.body.decode('utf-8'))
        room_id_list = jsonpath.jsonpath(res,'$..room_id')
        room_name_list = jsonpath.jsonpath(res,'$..room_name')
        room_src_list = jsonpath.jsonpath(res,'$..room_src')
        nickname_list = jsonpath.jsonpath(res,'$..nickname')
        for room_id,room_name,room_src,nickname in zip(room_id_list,room_name_list,room_src_list,nickname_list):
            item = DouyuItem()
            item['room_id'] = room_id
            item['room_name'] = room_name
            item['room_src'] = room_src
            item['nickname'] = nickname
            yield item
