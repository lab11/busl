import sched, time, urllib
from stop import *
import elementtree.ElementTree as ET

event_1_flag = False
event_2_flag = False
event_3_flag = False

def fire_event(event_type):
   print "firing event type " + str(event_type)

def check_events(toa, threshold):
   if toa <= threshold and toa >= threshold-3*60:
      fire_event(1)   
   elif toa >= threshold and toa <= threshold + 5*60:
      fire_event(2)
   elif toa >= threshold + 5*60 and toa <= threshold + 10*60:
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
         stop_good = False
         toa_list = []
         for stop in item: 
           if stop.tag == 'name':
             if stop.text == name:
               print "Monitoring " + stop.text + " on route: " + route_name 
               stop_good = True
           #TODO pretty bad hardcoding here....
           if stop.tag == 'toa1' and stop_good == True:
               toa_list.append(float(stop.text))
           if stop.tag == 'toa2' and stop_good == True:
               toa_list.append(float(stop.text))
           if stop.tag == 'toa3' and stop_good == True:
               toa_list.append(float(stop.text))
           if stop.tag == 'toa4' and stop_good == True:
               toa_list.append(float(stop.text))
           if stop.tag == 'toa5' and stop_good == True:
               toa_list.append(float(stop.text))
           if stop.tag == 'toacount' and stop_good == True:    
               while True:
                   if (len(toa_list) == 0):
                      break
                   toa = min(toa_list)
                   if (toa <= threshold-3*60):
                      toa_list.remove(min(toa_list))
                   else:
                      break
               print "\tWalking time: " + str(threshold/60) + " minutes"
               print "\tTime to arrival: " + str(toa/60) + " minutes"
               check_events(toa, threshold)
               stop_good = False
   #print "Beat"
   sc.enter(2,1,query_worker,(name, threshold, routes, sc,))

def query(name, threshold, routes):
   print 'Running Light Server!'
   s = sched.scheduler(time.time, time.sleep)
   s.enter(2,1,query_worker,(name,threshold,routes,s,))
   s.run()

#query('Murfin and Bonisteel N', 40, ['Northwood (Weekends)'])



