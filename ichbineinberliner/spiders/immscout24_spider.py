import scrapy
from ichbineinberliner.items import YummyBerlinerItem
import re
import logging

def make_numeric(string, func=float):
		string = re.sub("[^0-9,\.]", "", string).strip()
		string = string.replace(".", "")
		return func(string.replace(',', '.'))

def clean_encode(string):
	string = string.replace('\r\n', ' ').replace('\t', '').strip()
	string = ' '.join(string.split())
	string = string.encode('utf-8')
	return string


class ImmoScout24Spider(scrapy.Spider):
	name = "immoscout24"
	areas = ["kreuzberg", "schoeneberg", "charlottenburg"]  # ""
	allowed_domains = ["immobilienscout24.de"]
	root_urls = ["http://www.immobilienscout24.de/wohnen/berlin,berlin,{}-{}/mietwohnungen".format(area, area) for area in areas]
	start_urls = [root_url + ".html" for root_url in root_urls] + [root_url + ",seite-%s.html"  % page for page in xrange(2, 20) for root_url in root_urls]

	link_xpath = "h3/a/@href"
	wlist_xpath = '//div[@class="is24-res-list is24-res-gallery"]/ol/li'
	miete_xpath = 'div/dl[@class="is24-res-details"]/dd[1]/text()'
	sqm_xpath = 'div/dl[@class="is24-res-details"]/dd[2]/text()'
	zimmer_xpath = 'div/dl[@class="is24-res-details"]/dd[3]/text()'
	address_xpath = 'div/p[@class="is24-address"]/text()'

	def parse(self, response):
		# set german locale
		for sel in response.xpath(self.wlist_xpath):
			item = YummyBerlinerItem()
			item['link'] = 'http:' + sel.xpath(self.link_xpath).extract()[0]
			item['source_id'] = item['link'].split('/')[-1]
			item["miete"] = make_numeric(sel.xpath(self.miete_xpath).extract()[0])
			item["sqm"] = make_numeric(sel.xpath(self.sqm_xpath).extract()[0])
			item["zimmer"] = make_numeric(sel.xpath(self.zimmer_xpath).extract()[0])
			item["addr"] = clean_encode(sel.xpath(self.address_xpath).extract()[0])
			yield item
