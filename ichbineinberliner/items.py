# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YummyBerlinerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	source_id = scrapy.Field()
	link = scrapy.Field()
	addr = scrapy.Field()
	sqm  = scrapy.Field()
	miete = scrapy.Field()
	zimmer = scrapy.Field()
	time_to = scrapy.Field()  # time to destination using transit or driving
	url = scrapy.Field()
	lat = scrapy.Field()
	lng = scrapy.Field()
