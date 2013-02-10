import googlemaps

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
#   Src and dest lat/long
#Output:
#   distance (driving route) and time ("walking" along driving route)
def google_dist(src_lat, src_lng, dest_lat, dest_lng):
   try:
      directions = gmaps.directions((src_lat, src_lng), (dest_lat, dest_lng))
      distance = directions['Directions']['Distance']['meters']
      time = directions['Directions']['Duration']['seconds']
   except googlemaps.GoogleMapsError:
      print "Problem calculating distance to " + dest_lat + ", " + dest_lng
      distance = ERROR_VAL
      time = ERROR_VAL 
   return distance, walking_duration(time)

#Input: 
#   a src lat/long 
#   a list of Stop objects
#   how many of the closest stops to return
#Output:
#   the n closest stops 
def get_n_closest(src_lat, src_lng, stops, n):
   walking_info = [[google_dist(src_lat, src_lng, s.lat, s.lng), s] for s in stops]
   walking_info.sort()
   return walking_info[:n]

def get_n_closest(src_addr, stops, n):
   s_lat, s_lng = addr_to_latlng(src_addr)
   return get_n_closest(s_lat, s_lng, stops, n)


#All units are in seconds
def walking_duration(driving_duration):
   return driving_duration * 10
