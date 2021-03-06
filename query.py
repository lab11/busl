import sched, time, urllib
import hue
from stop import *
import elementtree.ElementTree as ET
from microcontroller import *

counter = 0
event_1_flag = False
event_2_flag = False
event_3_flag = False

#TODO Does not handle buses going the wrong way
#TODO Not tested with multiple routes... probably doesn't work
def fire_event(event_type, light):
   global event_1_flag
   global event_2_flag
   global event_3_flag
   if event_type == 1 and event_1_flag == False:
      event_1_flag = True
      event_2_flag = False
      event_3_flag = False
      hue.set_red(light)
      #fire("red")
   elif event_type == 1 and event_1_flag == True:
      print "\tfired event type " + str(event_type)
   elif event_type == 2 and event_2_flag == False:
      event_1_flag = False
      event_2_flag = True
      event_3_flag = False
      hue.set_purple(light)
      #fire("orange")
   elif event_type == 2 and event_2_flag == True:
      print "\tfired event type " + str(event_type)
   elif event_type == 3 and event_3_flag == False:
      event_1_flag = False
      event_2_flag = False
      event_3_flag = True
      hue.set_yellow(light)
      #fire("cyan")
   elif event_type == 3 and event_3_flag == True:
      print "\tfired event type " + str(event_type)
   else:
      event_1_flag = False
      event_2_flag = False
      event_3_flag = False
      hue.set_white(light)
      #fire("off")
      
def check_events(toa, threshold, light):
   if toa <= threshold and toa >= threshold-3*60:
      fire_event(1, light)   
   elif toa >= threshold and toa <= threshold + 5*60:
      fire_event(2, light)
   elif toa >= threshold + 5*60 and toa <= threshold + 10*60:
      fire_event(3, light)
   else: 
      fire_event(-1, light)

   return

def query_worker(name, threshold, routes, light, sc):
  global counter
  try:
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
                      print "\tTime to arrival: " + str(toa/60) + " minutes"
                      break
               print "\tWalking time: " + str(threshold/60) + " minutes"
               check_events(toa, threshold, light)
               stop_good = False
   #print "Beat"
   beat()
  except: 
   print "Skipped"
  print counter
  counter = counter + 1
  sc.enter(2,1,query_worker,(name, threshold, routes, light, sc,))

def query(name, threshold, routes, light):
   fire_event(1, light)
   s = sched.scheduler(time.time, time.sleep)
   s.enter(2,1,query_worker,(name,threshold,routes,light,s,))
   s.run()



