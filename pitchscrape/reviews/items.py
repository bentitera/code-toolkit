# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ReviewsItem(scrapy.Item):
	artists = scrapy.Field()
	album = scrapy.Field()
	url = scrapy.Field()
	text = scrapy.Field()
	score = scrapy.Field()
	date = scrapy.Field()
	genre = scrapy.Field()
	time = scrapy.Field()


class ImageItem(scrapy.Item):
    image_url = scrapy.Field()
    images = scrapy.Field()

