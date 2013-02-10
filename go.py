import sys, io, urllib
from time import time
from stop import *
import elementtree.ElementTree as ET

def get_all_umich_stops():
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
   
   stops = []
   for route in tree.findall('route'):
      for item in route:
         if item.tag == 'name':
            route_name = item.text
         if item.tag == 'stop':
            names = []
            for stop in item:
               if (stop.tag == 'name'):
                  if (stop.text != 'None'): 
                     names.append(stop.text)
               if (stop.tag == 'name2'):
                  if (stop.text != 'None'): 
                     names.append(stop.text)
               if (stop.tag == 'name3'):
                  if (stop.text != 'None'): 
                     names.append(stop.text)
               if (stop.tag == 'latitude'):
                  lat = stop.text
               if (stop.tag == 'longitude'):
                  lng = stop.text
	       if (stop.tag == 'id1'):
                  uid = stop.text
	    	  cur_stop = Stop(uid, names, ['UMICH'], [route_name], lat, lng)
		  stops.append(cur_stop)
   return stops

