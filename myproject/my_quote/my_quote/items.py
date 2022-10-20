# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass
# from scrapy.loader import ItemLoader
# from scrapy.loader.processors import Identity


@dataclass
class MyQuoteItem:
    # define the fields for your item here like:
    # name = scrapy.Field()
    quote: str
    author: str
    tags: list[str]

# class MyQuoteItemLoader(ItemLoader):
#