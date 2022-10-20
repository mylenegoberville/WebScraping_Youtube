import scrapy


class YoutubeSpider(scrapy.Spider):
    name = 'youtube'
    allowed_domains = ['https://wallhaven.cc/']
    start_urls = ['https://wallhaven.cc/']

    def parse(self, response):
        pass