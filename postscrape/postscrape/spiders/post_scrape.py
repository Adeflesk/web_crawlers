import scrapy

class PostSpider(scrapy.Spider):
    name = "posts"


    start_urls = [
        'https://blog.scrapinghub.com/page/1/',
        'https://blog.scrapinghub.com/page/2/'
    ]

