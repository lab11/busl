import googlemaps
import time
import math

ERROR_VAL = float("inf")

gmaps = googlemaps.GoogleMaps()

def addr_to_latlng(addr):
   try:
      lat, lng = gmaps.address_to_latlng(addr)
   except googlemaps.GoogleMapsError:
      lat, lng = ERROR_VAL, ERROR_VAL 
      print "We're not sure where that address is. Got anything better?"
   return lat, lng

#Input: 
#   a src lat/long 
#   a list of Stop objects
#   how many of the closest stops to return
#Output:
#   the n closest stops 
def order_by_latlng_distance(src_latlng, stops):
   walking_info = []
   for s in stops:
      dist_km = distance(src_latlng, (s.lat, s.lng))
      dur_min = walking_time(dist_km)
      walking_info.append([dur_min, dist_km*1000, s])
   walking_info.sort()
   return walking_info

def order_by_distance(src_addr, stops):
   return order_by_latlng_distance(addr_to_latlng(src_addr), stops)

def walking_time(dist_km):
   walking_speed = 5.0 #km/hr
   time_in_mins = (dist_km/walking_speed)*60
   time_in_mins += 3#to account for packing, stairs, etc.
   return time_in_mins

#Author: Wayne Dick
#www.platoscave.net/blog/2009/oct/5/calculate-distance-latitude-longitude-python
#Much thanks! 
def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d
