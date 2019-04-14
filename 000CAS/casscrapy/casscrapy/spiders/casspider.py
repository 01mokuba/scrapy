import scrapy

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from casscrapy.items import CasscrapyItem

class CasspiderSpider(CrawlSpider):
    # spiderの名称、クローリングの対象を設定
    name = 'casspider'
    allowed_domains = ['www.cas.go.jp']
    start_urls = ['https://www.cas.go.jp/']

    # ルールの設定
    rules = (
    # 指定URL以下、全てのページを対象にparse_pageinfoを実行
    Rule(LinkExtractor(allow=r'/'), callback='parse_pageinfo', follow=True),
    )

    # parse_pageinfoの定義
    def parse_pageinfo(self, response):
        sel = Selector(response)
        item = CasscrapyItem()
        item['URL'] = response.url
        # ページのどの部分をスクレイプするかを指定
        # ここではxPath形式でタイトルタグのテキストを指定
        item['title'] = sel.xpath('/html/head/title/text()').extract()
        return item
