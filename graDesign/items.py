# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GradesignItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ProductiesItem(scrapy.Item):
    # brief_introduction = scrapy.Field()
    # brand = scrapy.Field()
    # product_name = scrapy.Field()
    # product_id = scrapy.Field()
    # price = scrapy.Field()

    # 测试用
    # item["brand"], item["store"], item["brief_introduction"], item["price"],
    # item["variety"], item["product_id"], item["authenticate_moder"], item["url"],
    # item["crawl_time_stamp"], item["crawl_time_Ymd"], item["crawl_time_Hms"],
    brand = scrapy.Field()
    store = scrapy.Field()
    brief_introduction = scrapy.Field()
    price = scrapy.Field()
    variety = scrapy.Field()
    product_id = scrapy.Field()
    authenticate_moder = scrapy.Field()
    url = scrapy.Field()
    crawl_time_stamp = scrapy.Field()
    crawl_time = scrapy.Field()


    # 时间
    # time_stamp = scrapy.Field()
    # time_Ymd = scrapy.Field()
    # time_Hms = scrapy.Field()

    # store = scrapy.Field()
    # url = scrapy.Field()
    # variety = scrapy.Field()
    # product_area = scrapy.Field()
    # system = scrapy.Field()


