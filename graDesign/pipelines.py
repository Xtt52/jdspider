# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import MySQLdb.cursors

from twisted.enterprise import adbapi


class GradesignPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlTwistedPipline(object):
    # 采用异步机制插入数据
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host = settings["MYSQL_HOST"],
            db = settings["MYSQL_DBNAME"],
            user = settings["MYSQL_USER"],
            passwd = settings["MYSQL_PASSWORD"],
            charset = 'utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode = True
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)

        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted将mysql插入变为异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider)  # 处理异常

    def handle_error(self, failure, item, spider):
        # 处理异步插入的异常
        print(failure)

    def do_insert(self, cursor, item):
        # 执行具体的插入

        # insert_sql = """
        #     insert into productiesTest(product_id, brand, product_name, brief_introduction, price, time_stamp, time_Ymd, time_Hms)
        #     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        # """
        # cursor.execute(insert_sql, (item["product_id"], item["brand"], item["product_name"], item["brief_introduction"],
        #                             item["price"], item["time_stamp"], item["time_Ymd"], item["time_Hms"]))
        # cursor.execute(insert_sql, (item["title"], item["create_date"], item["url"], item["url_object_id"],
        #                             item["front_image_url"], item["front_image_path"], item["comment_nums"],
        #                             item["fav_nums"], item["praise_nums"], item["tags"]))

        insert_sql = """
            insert into products_info(brand, store, brief_introduction, price, variety, product_id, authenticate_moder, 
                                     url,crawl_time_stamp, crawl_time)
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        # insert_sql = """
        #             insert into product_info(brand, store, brief_introduction, price, variety, product_id, authenticate_moder,
        #                                     url,crawl_time_stamp, crawl_time_Ymd, crawl_time_Hms)
        #              values (%(args1,args2,args3,args4,args5,args6,args7,args8,args9,args10,args11))
        #         """

        cursor.execute(insert_sql, (item["brand"], item["store"], item["brief_introduction"], item["price"],
                                    item["variety"], item["product_id"], item["authenticate_moder"], item["url"],
                                    item["crawl_time_stamp"], item["crawl_time"]))

        print("插入成功！！！")

