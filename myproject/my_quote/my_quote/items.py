# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass, field
from typing import Optional
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose


@dataclass
class MyQuoteItem:
    quote: Optional[str] = field(default=None)
    author: Optional[str] = field(default=None)
    tags: Optional[list[str]] = field(default_factory=list)


class MyQuoteItemLoader(ItemLoader):

    @staticmethod
    def _my_lower(s: str) -> str:
        return s.lower()

    # とりあえずお試しで適当にprocessorを指定してみる
    quote_in = MapCompose(str.title)
    author_in = MapCompose(str.upper)
    tags_in = MapCompose(_my_lower)
