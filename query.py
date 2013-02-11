import sched, time, urllib
from stop import *
import elementtree.ElementTree as ET

def fire_event(event_type):
   print "firing event type " + str(event_type)

def check_events(toa, threshold):
   if toa <= threshold:
      fire_event(1)   
   elif toa >= threshold and toa <= threshold + 5:
      fire_event(2)
   elif toa >= threshold + 5 and toa <= threshold + 10:
      fire_event(3)

def query_worker(name, threshold, routes, sc):
   magic_bus_xml_url = 'http://mbus.pts.umich.edu/shared/public_feed.xml'
   magic_bus_xml_socket = urllib.urlopen(magic_bus_xml_url)
   magic_bus_xml = magic_bus_xml_socket.read()
   magic_bus_xml_socket.close()
   #print "Looking for " + name + " on routes: " + str(routes)
   tree = ET.fromstring(magic_bus_xml)
   for route in tree.findall('route'):
     skip = False
     for item in route:
       if item.tag == 'name':
         if not item.text in routes:
            skip = True
         else:
            route_name = item.text
       if item.tag == 'stop' and skip == False:         
         stop_good = False;
         for stop in item: 
           if stop.tag == 'name':
             if stop.text == name:
               #print "Hit on: " + stop.text + " on route: " + route_name 
               stop_good = True
           if stop.tag == 'toa1' and stop_good == True:
               toa = float(stop.text)
               adjusted_toa = toa + threshold
               print "time to arrival: " + stop.text
               print "adjusted time: " + str(adjusted_toa) 
               check_events(toa, threshold)
               stop_good = False
   #print "Up'd"
   sc.enter(2,1,query_worker,(name, threshold, routes, sc,))

def query(name, threshold, routes):
   #print 'Running!'
   s = sched.scheduler(time.time, time.sleep)
   s.enter(2,1,query_worker,(name,threshold,routes,s,))
   s.run()

#query('Murfin and Bonisteel N', 40, ['Northwood (Weekends)'])



