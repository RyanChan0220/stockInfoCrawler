__author__ = 'RyanChan'

from scrapy.spider import Spider


class LeTVSpider(Spider):
    name = "LeTV"
    allowed_domains = ["sina.com.cn"]
    