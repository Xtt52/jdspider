# -*- coding: utf-8 -*-
import requests
import scrapy
import json
import re
import time, datetime

from scrapy.http import Request
from urllib import parse
from graDesign.items import ProductiesItem


class JdspiderSpider(scrapy.Spider):
    name = 'jdSpider'
    # allowed_domains = ['list.jd.com/list.html?cat=670%2C671%2C672']
    # 爬取 联想 品牌的爬虫
    start_urls = ['https://list.jd.com/list.html?cat=670,671,672&ev=exbrand_11516']
    # page_count = 5

    def parse(self, response):
        next_urls = response.css('a.pn-next::attr(href)').extract()[0]
        if next_urls:
            # self.page_count = self.page_count-1
            yield Request(url=parse.urljoin(response.url, next_urls), callback=self.parse)

        brand_nodes = response.css("li.gl-item div.p-img a::attr(href)").extract()
        for brand_url in brand_nodes:
            yield Request(url=parse.urljoin(response.url, brand_url), callback=self.parse_detail)

    def parse_detail(self, response):
        products_item = ProductiesItem()

        res = response.css("div.p-parameter .parameter2 li *::text").extract()
        brief_info = response.css("div.sku-name::text").extract()
        brief_info_str = brief_info[0].replace(' ', '')
        brief_info_str = brief_info_str.replace('\n', '')
        products_item["brief_introduction"] = brief_info_str

        brand = response.css('ul#parameter-brand a::text').extract()[0].replace(' ', '')
        products_item["brand"] = brand

        match_re = re.match(".*：(.*)", res[0])
        if match_re:
            product = match_re.group(1)
        else:
            product = ""

        products_item["variety"] = product

        match_re = re.match(".*?(\d+).*", res[1])
        if match_re:
            product_id = int(match_re.group(1))
        else:
            product_id = -1
        products_item["product_id"] = str(product_id)

        # 获取价格
        price_url = "https://p.3.cn/prices/mgets?skuIds=" + str(product_id)
        p_json = requests.get(url=price_url).content.decode()
        pjson = json.loads(p_json)
        price = pjson[0]['p']
        products_item["price"] = price

        url = response.url
        products_item["url"] = url

        store = response.css('div.J-hove-wrap.EDropdown.fr div.name a::text').extract()[0]
        products_item["store"] = store

        # 提取3C认证编号
        s = response.css('div.Ptable .Ptable-item')
        authenticate_moder = ""
        for selector in s:
            if selector.css('h3::text').extract()[0] == "主体":
                authenticate_moder = selector.xpath('dl/dl[last()]/dd[last()]/text()').extract()[0]
        products_item["authenticate_moder"] = authenticate_moder

        # 以完成products_item["brand"] = "联想"
        # 以完成products_item["store"] = "联想北达兴科专卖店"
        # 以完成products_item["brief_introduction"] = "联想（Lenovo）昭阳E43-80(E42-80升级版) 14英寸高端商务办公酷睿i5笔    记本电脑 定制i5-8250U 8G 1T+128G固态 2G独显 高清屏"
        # 以完成products_item["price"] = 4399
        # 以完成products_item["variety"] = "联想小新Air"
        # 以完成products_item["product_id"] = 37857301878
        # products_item["authenticate_moder"] = "E43-80"
        # 以完成products_item["url"] = "https://item.jd.com/37857301878.html"

        # 时间
        time_stamp = int(time.time())
        timeArray = time.localtime(time_stamp)
        time_Ymd = time.strftime("%Y-%m-%d", timeArray)
        time_Hms = time.strftime(" %H:%M:%S", timeArray)
        # dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        products_item["crawl_time_stamp"] = time_stamp
        products_item["crawl_time"] = time_Ymd+time_Hms

        # print(price)
        print("ok...")

        return products_item
