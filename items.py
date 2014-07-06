__author__ = 'RyanChan'

from scrapy.item import Item, Field


class Transaction(Item):
    title = Field()
    value = Field()
    type = Field()