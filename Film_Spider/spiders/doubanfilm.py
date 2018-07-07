# -*- coding: utf-8 -*-
import scrapy
import Film_Spider.items

class DoubanfilmSpider(scrapy.Spider):
        name = "doubanfilm"
        allowed_domains = ["movie.douban.com"]
        start_urls = [
           "https://movie.douban.com/tag/%E5%89%A7%E6%83%85"
        ]

        def parse(self, response):
            for info in  response.xpath('//tr[@class="item"]/td[2]/div/a/@href'):
              url = info.extract()
             # print (url + "\n")
              yield scrapy.Request(url, callback=self.parse_each_movie)

            next_page = response.xpath('//span[@class="next"]/a/@href').extract()
            if next_page:
                print('--------------Finding next page: [%s] --------------------------'), next_page
                yield scrapy.Request(next_page[0], callback=self.parse)
            else:
                print('--------------There is no more page!--------------------------')


        def parse_each_movie(self, response):
            item = Film_Spider.items.DoubanItem()
            item['movie_name'] = response.xpath('//span[@property="v:itemreviewed"]/text()')[0].extract()
            item['movie_date'] = response.xpath('//span[@property="v:initialReleaseDate"]/text()')[0].extract()
            item['movie_time'] = response.xpath('//span[@property="v:runtime"]/@content')[0].extract()
            item['movie_star'] = response.xpath('//strong[@property="v:average"]/text()')[0].extract()
            # print (item)
            print ("scrapy success!!! \n\n\n\n")
            return item

class ProxieSpider(scrapy.Spider):

    name = "proxie"
    allowed_domains = ["sina.com.cn"]
    start_urls = ['http://news.sina.com.cn/']
    def parse(self, response):
        print(response.body)
