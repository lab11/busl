class Stop:
   """
   A bus stop representation.
      - uid is a unique identifier used by the program
      - names are the names of the stop
      - lat and lng are the location
   """
   def __init__(self, uid, names, systems, active_routes, lat, lng):
      self.uid = uid
		self.names = names
		self.systems = systems
		self.active_routes = active_routes
		self.lat = lat
      self.lng = lng
