import scrapy
from dalecooper_scrapy.items import DalecooperScrapyItem

class DalecooperSpider(scrapy.Spider):
    name = 'dalecooper'
    allowed_domains = ["imdb.com"]
    start_urls = ['http://www.imdb.com/character/ch0009681/quotes']

    def parse(self, response):
        for sel in response.xpath('//i/a'):
            item = DalecooperScrapyItem()
            item['quote'] = sel.xpath('//i[a[@href="/name/nm0001492/"]]/following-sibling::text()[1]').extract()
            yield item
