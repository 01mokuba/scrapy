import scrapy


class CasscrapyItem(scrapy.Item):
    # URLとtitleのフィールドを作成
    URL = scrapy.Field()
    title = scrapy.Field()
