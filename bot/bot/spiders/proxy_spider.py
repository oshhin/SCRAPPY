# bot/spiders/proxy_spider.py

import scrapy

class ProxySpider(scrapy.Spider):
    name = "proxy_spider"
    start_urls = ["http://www.example.com"]

    def parse(self, response):
        self.log(f"Visited {response.url}")
        self.log(response.text[:100])  # Log the first 100 characters of the response
