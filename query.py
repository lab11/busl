import sys, sched, time, io, urllib
from stop import *
import elementtree.ElementTree as ET


def query_worker(name, threshold, routes, sc):
   magic_bus_xml_url = 'http://mbus.pts.umich.edu/shared/public_feed.xml'
   magic_bus_xml_socket = urllib.urlopen(magic_bus_xml_url)
   magic_bus_xml = magic_bus_xml_socket.read()
   magic_bus_xml_socket.close()
   print "Looking for " + name + " on routes: " + str(routes)
   tree = ET.fromstring(magic_bus_xml)
   for route in tree.findall('route'):
     skip = False
     for item in route:
       if item.tag == 'name':
         if not item.text in routes:
            skip = True
       if item.tag == 'stop' and skip == False:
         for stop in item: 
           if stop.tag == 'name':
             if stop.text == name:
               print "Hit on: " + stop.text
   print "Up'd"
   sc.enter(2,1,query_worker,(name, threshold, routes, sc,))

def query(name, threshold, routes):
   print 'Running!'
   s = sched.scheduler(time.time, time.sleep)
   s.enter(2,1,query_worker,(name,threshold,routes,s,))
   s.run()


query('Murfin and Bonisteel N',50, ['Northwood (Weekends)'])


