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


for route in tree.findall('route'):
   for item in route:
      if item.tag == 'name':
        all_routes.append(item.text)
      if item.tag == 'id':
	print item.text
      if item.tag == 'stop':
        for stop in item:
           if (stop.tag == 'name' 
                or stop.tag == 'name2'
                or stop.tag == 'name3'):
              if (stop.text != 'None'):
                 print stop.text
 
print all_routes            
