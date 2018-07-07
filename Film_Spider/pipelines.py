# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql
from collections import Counter

class DBPipeline(object):
    def process_item(self, item, spider):

            con = pymysql.connect(host='localhost', user="root", passwd="root", db="doubandb", charset="utf8", port=3306)
            cur = con.cursor()
            try:
                cur.execute(
                    """insert into movie_info(movie_name,movie_date,movie_time,movie_star)values(%s, %s, %s, %s)""",
                    (str(item['movie_name']).split()[0],
                     str(item['movie_date'])[0:4],
                     item['movie_time'],
                     item['movie_star']))
            # 提交sql语句
                con.commit()
                print ("mysql insert success !!! \n\n\n")
                cur.close()
                con.close()
            except Exception as error:
                print ('error\n')
                list = item['movie_name'] + item['movie_date'] +  item['movie_time'] + item['movie_star'] ;
              #  print (list)

            return item





