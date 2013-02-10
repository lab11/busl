import sys, io, urllib
from time import time
import elementtree.ElementTree as ET

##################
# Static Variables
##################
magic_bus_xml_url = 'http://mbus.pts.umich.edu/shared/public_feed.xml'

####################
# Download the stuff
####################
magic_bus_xml_socket = urllib.urlopen(magic_bus_xml_url)
magic_bus_xml = magic_bus_xml_socket.read()
magic_bus_xml_socket.close()


#Build the XML tree
tree = ET.fromstring(magic_bus_xml)

all_routes = []

address_input = raw_input("Enter an address: ")

stops = []
for route in tree.findall('route'):
   for item in route:
      if item.tag == 'name':
        all_routes.append(item.text)
      #if item.tag == 'id':
	#print item.text
      if item.tag == 'stop':
        stop_dict = {}
        name_dict = {}
        for stop in item:
           if (stop.tag == 'name'):
              if (stop.text != 'None'): 
               name_dict['1'] = stop.text
           if (stop.tag == 'name2'):
              if (stop.text != 'None'): 
               name_dict['2'] = stop.text
           if (stop.tag == 'name3'):
              if (stop.text != 'None'): 
               name_dict['3'] = stop.text
               stop_dict['name'] = name_dict 
           if (stop.tag == 'latitude'):
             stop_dict['lat'] = stop.text
           if (stop.tag == 'longitude'):
             stop_dict['lng'] = stop.text
             stops.append(stop_dict)

print stops
