class Stop:
	"""
	A bus stop representation.
	   - uid is a unique identifier used by the program
		- names is a dictionary of possible names
		- lat and lng are the location
	"""
	def __init__(self, uid, names, lat, lng):
      self.uid = uid
		self.names = names
		self.lat = lat
		self.lng = lng
