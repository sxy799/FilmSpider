
BOT_NAME = 'Film_Spider'

SPIDER_MODULES = ['Film_Spider.spiders']
NEWSPIDER_MODULE = 'Film_Spider.spiders'


#这些都是你的数据库登录的一些数据

MYSQL_HOST='127.0.0.1'
MYSQL_USER='root'

#你自己数据库的密码
MYSQL_PASSWORD='root'
MYSQL_PORT =3306

#你自己数据库的名称
MYSQL_DB='doubandb'
CHARSET='utf8'

COOKIES_ENABLED = False


USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'



# DOWNLOADER_MIDDLEWARES = {
# #    'myproxies.middlewares.MyCustomDownloaderMiddleware': 543,
#      'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':543,
#      'Film_Spider.middlewares.MyproxiesSpiderMiddleware':125
# }

ITEM_PIPELINES = {
    'Film_Spider.pipelines.DBPipeline': 50
}

IPPOOL=[
    {"ipaddr":"114.228.74.31:6666"},
    {"ipaddr":"121.231.32.171:6666"},
    {"ipaddr":"222.186.45.146:63756"},
    {"ipaddr":"114.228.73.204:6666"},
    {"ipaddr":"112.95.207.163:9999"}
]