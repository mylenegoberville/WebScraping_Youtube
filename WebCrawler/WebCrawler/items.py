# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ReviewsAllocineItem(scrapy.Item):
    title = scrapy.Field()
    img = scrapy.Field()
    author = scrapy.Field()
    genre = scrapy.Field()
    score = scrapy.Field()
    desc = scrapy.Field()
    time = scrapy.Field()
    release = scrapy.Field()

class ReviewsYoutubeItem(scrapy.Item):
    title = scrapy.Field()
    category = scrapy.Field()
    author = scrapy.Field()
    img = scrapy.Field()
    view = scrapy.Field()
    desc = scrapy.Field()
    release = scrapy.Field()
    
class ReviewsWallhavenItem(scrapy.Item):
    user_name = scrapy.Field()
    last_active = scrapy.Field()
    joined = scrapy.Field()
    uploads = scrapy.Field()
    views = scrapy.Field()
    favorites = scrapy.Field()
    subscribe = scrapy.Field()
    comments = scrapy.Field()
    posts = scrapy.Field()
    wallpapers_tagged = scrapy.Field()
    Wallpapers_flagged = scrapy.Field()