import scrapy
from scrapy import Request
from WebCrawler.items import ReviewsWallhavenItem
import time

class WallhavenSpider(scrapy.Spider):
    name = 'wallhaven'
    allowed_domains = ['wallhaven.cc']
    
    #Pas encore automatiser mais en changeant l'url manuellement on peut obtenir plusieurs utilisateurs dans le CSV
    #start_urls = ['https://wallhaven.cc/user/JustJon']
    start_urls = ['https://wallhaven.cc/user/jofire']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_wallhaven)
            
    def parse_wallhaven(self, response):
        item = ReviewsWallhavenItem()
        liste_items = response.css('dd')
        
        #user name
        try: 
            item['user_name'] = response.css('h1.username').css('a::text').extract()
        except:
            item['user_name'] = 'None'
        
        #last active
        try: 
            item['last_active'] = liste_items[0].css('time::text').extract()
        except:
            item['last_active'] = 'None'

        #years of inscription
        try: 
            item['joined'] = liste_items[1].css('time::text').extract()
        except:
            item['joined'] = 'None'

        #number of upload
        try: 
            item['uploads'] = liste_items[2].css('::text').extract()
        except:
            item['uploads'] = 'None'

        #number of views
        try: 
            item['views'] = liste_items[3].css('::text').extract()
        except:
            item['views'] = 'None'

        #favorites wallpaper
        try: 
            item['favorites'] = liste_items[4].css('::text').extract()
        except:
            item['favorites'] = 'None'

        #number of subscribers
        try: 
            item['subscribe'] = liste_items[5].css('::text').extract()
        except:
            item['subscribe'] = 'None'

        #number of comments
        try: 
            item['comments'] = liste_items[6].css('::text').extract()
        except:
            item['comments'] = 'None'

        #number of posts
        try: 
            item['posts'] = liste_items[7].css('::text').extract()
        except:
            item['posts'] = 'None'

        #number of wallpaper tagged
        try: 
            item['wallpapers_tagged'] = liste_items[8].css('::text').extract()
        except:
            item['wallpapers_tagged'] = 'None'

        #number of wallpaper flagged
        try: 
            item['Wallpapers_flagged'] = liste_items[9].css('::text').extract()
        except:
            item['Wallpapers_flagged'] = 'None'

        yield item