import scrapy


class BoursoramaSpider(scrapy.Spider):
    name = 'boursorama'
    allowed_domains = ['www.boursorama.com']
    start_urls = ['http://www.boursorama.com/']

    def parse(self, response):
        pass
