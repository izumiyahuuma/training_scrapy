import scrapy


class QuotesSpider(scrapy.Spider):
    # プロジェクト内でユニークである必要がある
    name = "quotes"

    # start_requestsで特別何かしたいことがなければ、
    # 予め回りたいurlのリストを記載しておくことも可能。
    # start_urls = [
    #     'https://quotes.toscrape.com/page/1/',
    #     'https://quotes.toscrape.com/page/2/',
    # ]

    # ジェネレータ関数 or listを返すような形にしないといけない
    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall()
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
