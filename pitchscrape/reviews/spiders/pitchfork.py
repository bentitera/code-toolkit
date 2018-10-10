# -*- coding: utf-8 -*-
import scrapy
import pandas as pd 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

#here is where we start from
BASE_URL = 'https://pitchfork.com'

#Here is where we will store the items we scrape
class ReviewItem(scrapy.Item):
    artists = scrapy.Field()
    album = scrapy.Field()
    url = scrapy.Field()
    text = scrapy.Field()
    score = scrapy.Field()
    genre = scrapy.Field()
    time = scrapy.Field()
    image_urls = scrapy.Field()
    image = scrapy.Field()

#Here is where we scrape
class PitchforkSpider(CrawlSpider):
    name = 'pitchfork'
    allowed_domains = ['pitchfork.com']
    #this is a list of urls that are a product of seeing the pattern of urls
    #in pitchfork reviews
    start_urls = ['https://pitchfork.com/reviews/albums/?page=' + str(i) for i in range(1, 4)]


    rules = [Rule(LinkExtractor(allow = ''), callback = 'parse', follow = True)]

    #Here is where we actually get information from the pages that we tested in
    #our terminal
    def parse(self, response):
        artists = response.xpath('//ul/li[1]/text()').extract()
        album = response.xpath('//h2/text()').extract()
        urls = response.xpath('//div[@class = "review"]/a/@href').extract()
        #create the urls to follow
        url = [BASE_URL + link for link in urls]
        #we follow the urls that lead to the larger review
        for link in url:
                request = scrapy.Request(link, callback = self.review_text,
                dont_filter = True)
                yield request

    #here we extract information from the page containing information about the full review
    def review_text(self, response):
            text = response.xpath('//p/text()').extract()
            title = response.xpath('//h2/ul/li/a/text()').extract()
            album = response.xpath('//h1/text()').extract()
            score = response.xpath('//span[@class="score"]/text()').extract()
            genre = response.xpath('//a[@class="genre-list__link"]/text()').extract()
            time = response.xpath('//time/text()').extract()


            #Here, we output the information scraped which allows us to store it as a file
            yield ReviewItem(
                artists= title,
                album = album,
                text = text,
                score = score,
                genre = genre,
                time = time,
            )

    def parse_book(self, response):
        book = ReviewItem()
        relative_img_urls = response.css("div.item.active > img::attr(src)").extract()
        book["image_urls"] = self.url_join(relative_img_urls, response)

        return book

    def url_join(self, urls, response):
        joined_urls = []
        for url in urls:
            joined_urls.append(response.urljoin(url))

        return joined_urls

