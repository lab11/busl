import googlemaps as GoogleMaps

gmaps = GoogleMaps()

def addr_to_latlng(addr):
	try:
		lat, lng = gmaps.address_to_latlng(address)
	except GoogleMaps.GoogleMapsError:
		lat, lng = 0, 0
		print "We're not sure where that address is. Got anything better?"
	return lat, lng

def google_dist(lat1, lng1, lat2, lng2):
   return 0

#Input: 
#   one src lat/lng 
#   a list of potential destination structures
#   how many of the closest locations to return
#Output:
#   the n closest stops in structured form 
def get_N_closest(src_latlng, stops, n):
   return 


#All units are in seconds
def walking_duration(driving_duration):
	return driving_duration * 10
