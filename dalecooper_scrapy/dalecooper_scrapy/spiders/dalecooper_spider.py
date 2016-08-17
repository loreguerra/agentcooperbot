import scrapy
from dalecooper_scrapy.items import DalecooperScrapyItem
from scrapy.selector import Selector
import re

class DalecooperSpider(scrapy.Spider):
    name = 'dalecooper'
    allowed_domains = ["imdb.com"]
    start_urls = ['http://www.imdb.com/character/ch0009681/quotes']

    def parse(self, response):
        sel = Selector(response)
        for line in sel.xpath('//i[a[@href="/name/nm0001492/"]]/following-sibling::text()[1]').extract():
            line = str(line)
            quote = re.sub(r'\s{2,}|[\r\n\:\[]', "", line)
            item = DalecooperScrapyItem()
            item['quote'] = quote
            yield item


# line re.sub \n, line to string, string spli(' '), string join?
