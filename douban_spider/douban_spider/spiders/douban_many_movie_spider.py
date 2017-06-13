from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor

from douban_spider.items import DoubanSpiderItem

class DoubanSpider(CrawlSpider):

    name="douban_many_movie_spider"

    download_delay=1

    allowed_domains=["movie.douban.com"]

    start_urls=[
        'https://movie.douban.com/top250?start=0&filter=&type='
    ]

    rules=(
        Rule(LinkExtractor(allow=(r'https://movie\.douban\.com/top250\?start=\d+&filter=')),callback='parse_item',follow=True),
    )


    def parse_item(self,response):

        print response

        sel=Selector(response)
        item=DoubanSpiderItem()

        movie_name=sel.xpath('//span[@class="title"][1]/text()').extract()
        #movie_playable=sel.xpath('//div[@class="hd"]/text()').extract()
        star=sel.xpath('//div[@class="star"]/span[@class="rating_num"]/text()').extract()
        quote=sel.xpath('//p[@class="quote"]/span[@class="inq"]/text()').extract()


        item['movie_name']=[n.encode('utf-8')  for n in movie_name]
        #item['movie_playable']=[n.encode('utf-8') for n in movie_playable]
        item['star']=[n.encode('utf-8')  for n in star]
        item['quote']=[n.encode('utf-8')  for n in quote]


        yield item