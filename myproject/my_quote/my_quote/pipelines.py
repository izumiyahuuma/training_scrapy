# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from itemadapter import ItemAdapter
from scrapy import Spider
from scrapy.item import Item
from scrapy.exceptions import DropItem
from my_quote.items import MyQuoteItem
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class MyQuotePipeline:
    _EXTRACT_TAGS = ['love', 'inspirational', 'life', 'humor', 'books']

    def open_spider(self, spider: Spider):
        self.file = open('item.jsonl', 'w')
        pass

    def close_spider(self, spider: Spider):
        self.file.close()

    def process_item(self, item: Item, spider: Spider):
        adapter: ItemAdapter = ItemAdapter(item)
        if adapter.is_item_class(MyQuoteItem):
            # 試しに20px以上で書かれていたタグだけ抜き出してみる
            my_quote_item: MyQuoteItem = adapter.item
            if not any(map(my_quote_item.tags.__contains__, self._EXTRACT_TAGS)):
                raise DropItem()

        self.file.write(json.dumps(ItemAdapter(item).asdict()) + "\n")
        return item
