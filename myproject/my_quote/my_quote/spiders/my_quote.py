""" Quotesスクレイパー
https://quotes.toscrape.com/
へアクセスして名言、著者、タグを取得する。
「Next」リンクがなくなったら終了する。
"""

import scrapy
import logging
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.link import Link
from my_quote.items import MyQuoteItem, MyQuoteItemLoader

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

QUOTE_XPATHS: dict = {
    'quote_boxes': '//html/body/div/div[2]/div[1]/div',
    'page_transitions': '/html/body/div/div[2]/div[1]/nav/ul/li/a'
}


class MyQuote(scrapy.Spider):
    name: str = 'my_quote'
    link_extractor: LxmlLinkExtractor = LxmlLinkExtractor()

    def start_requests(self):
        url: str = "https://quotes.toscrape.com/"
        logger.info('start my_quote')
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: scrapy.http.Response, **kwargs):
        logger.info(f'visit : {response.url}')
        quote_boxes: list[scrapy.selector.Selector] = response.xpath(QUOTE_XPATHS['quote_boxes'])
        for index, box in enumerate(quote_boxes):
            logger.info(f'get {index + 1} / {len(quote_boxes)} quote.')

            # quote: str = box.xpath('./span[1]/text()').get()
            # author: str = box.xpath('./span[2]/small/text()').get()
            # tags: list[str] = box.xpath('./div/a/text()').getall()

            loader = MyQuoteItemLoader(item=MyQuoteItem(), selector=box)
            loader.add_xpath('quote', './span[1]/text()')
            loader.add_xpath('author', './span[2]/small/text()')
            loader.add_xpath('tags', './div/a/text()')
            yield loader.load_item()

        links: list[Link] = self.link_extractor.extract_links(response)
        for link in links:
            if 'Next' in link.text:
                yield response.follow(link.url, self.parse)

        # タグ要素とかで判断したいならxpath使って判定していく方が良さげ
        # next_link: str = self.search_next_page_link(response)
        # if next_link is not None:
        #     yield response.follow(next_link, self.parse)

    @staticmethod
    def search_next_page_link(response: scrapy.http.Response) -> str:
        """
        次のページへ遷移するためのリンクを探す
        :param response:
        :return: href
        """
        links: list[scrapy.selector.Selector] = response.xpath(QUOTE_XPATHS['page_transitions'])
        next_links: list[scrapy.selector.Selector] = list(filter(lambda x: 'Next' in x.xpath('./text()').get(), links))
        if len(next_links) > 0:
            return next_links[0].attrib['href']
