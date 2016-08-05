import scrapy

class DalecooperSpider(scrapy.Spider):
    name = 'dalecooper'
    allowed_domains = ["imdb.com"]
    start_urls = ['http://www.imdb.com/character/ch0009681/quotes']

    def parse(self, response):
        pass
