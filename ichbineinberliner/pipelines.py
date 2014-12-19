# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import simplejson, urllib

# url = "http://maps.googleapis.com/maps/api/directions/json?origin={0}&destination={1}&sensor=false&departure_time=1421312400&mode=transit"
# #url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=transit&departure_time=1421312400&language=en-EN&sensor=false"
# orig = wohnungs[0]["addr"].encode("utf-8")
# dest = (52.444311,13.273748)
# url = url.format(orig,str(dest))
# result= simplejson.load(urllib.urlopen(url))
# driving_time = result['routes'][0]['legs'][0]['duration']['value']
# driving_time



class IchbineinberlinerPipeline(object):
    def process_item(self, item, spider):
        return item

class AddDistanceToMPIPipeline(object):

	latlong_mpi =  str((52.444311,13.273748))
	url = "http://maps.googleapis.com/maps/api/directions/json?origin={0}&destination={1}&sensor=false&departure_time=1421312400&mode=transit"

	def process_item(self, item, spider):
		orig = item["addr"] #.encode("utf-8","ignore")
		dest = self.latlong_mpi
		url = self.url.format(orig, dest)
		result= simplejson.load(urllib.urlopen(url))
		time = result['routes'][0]['legs'][0]['duration']['value']/60.
		item["time_to"] = time
		return item
	
