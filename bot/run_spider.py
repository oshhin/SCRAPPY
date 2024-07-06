# MAKE SURE TO CHANGE THE PROXIES
# run_spider.py

from scrapy.crawler import CrawlerProcess
from bot.spiders.proxy_spider import ProxySpider

process = CrawlerProcess(settings={
    "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    'RETRY_TIMES': 10,
    'RETRY_HTTP_CODES': [500, 502, 503, 504, 522, 524, 408, 429],
    'DOWNLOADER_MIDDLEWARES': {
        'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
        'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
        'scrapy_proxies.RandomProxy': 100,
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
        'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
    },
    'AUTOTHROTTLE_ENABLED': True,
    'AUTOTHROTTLE_START_DELAY': 1,
    'AUTOTHROTTLE_MAX_DELAY': 60,
    'AUTOTHROTTLE_TARGET_CONCURRENCY': 1.0,
    'AUTOTHROTTLE_DEBUG': False,
    'PROXY_LIST': 'proxy_list.txt',
    'USER_AGENT_LIST': 'user_agent_list.txt'
})

process.crawl(ProxySpider)
process.start()
