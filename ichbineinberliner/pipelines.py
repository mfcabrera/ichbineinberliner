# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import simplejson, urllib
import googlemaps


class IchbineinberlinerPipeline(object):
    def process_item(self, item, spider):
        return item

class AddDistanceToMPIPipeline(object):

    latlong_mpi = str((52.444311, 13.273748))

    def __init__(self, ):
	self.gm_client = googlemaps.Client("")

    def process_item(self, item, spider):
	orig = item["addr"]
	geoloc = self.gm_client.geocode(orig)

	if len(geoloc) > 0:
	    for k in ('lat', 'lng'):
		item[k] = geoloc[0]['geometry']['location'][k]

	directions_result = self.gm_client.directions(str((item['lat'], item['lng'])),
						      self.latlong_mpi,
						      mode="transit",
						      departure_time=1421307820)

	#  Pick the fastest way
	chosen_leg = None
	if len(directions_result) > 0:
	    for dr in directions_result:
		for l in dr["legs"]:
		    if chosen_leg is None:
			chosen_leg = l
		    if chosen_leg is not None and \
		       chosen_leg["duration"]["value"] > l["duration"]["value"]:
			chosen_leg = l

	if chosen_leg is None:
	    return
	item["time_to"] = chosen_leg["duration"]["value"]/60.0
	return item
