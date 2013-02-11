import go
import maplib
from get_input import *
from system_setup import *
from query import *
from microcontroller import *


def main():
   options_per_page = 5

   print """
  -------------------------
  |   Welcome to BUS-L!   |
  -------------------------
  """
   #SYSTEM SETUP
   #Check for network access
   if internet_on() == False:
      print "No Internet = No BUSL! \n Please Check Your Interwebs" 
      return -1      
   

   ports = get_ports()
   if len(ports) != 0:
     #Set up GPIO for hardware
     print """
  -------------------------
  | Select Serial Port: |
  -------------------------"""
     display_serial_ports(ports, 0)
     index = get_user_int("\nPlease pick a serial port for the Arduino: ", len(ports))
     #if test_hardware(ports[index]) == False:
     #   print "No Microcontroller = No BUSL Lights! \n Please Check Your Ports"
    
   

   #USER CONFIG
   location = get_user_addr()
   
   #find X closest stops to user
   all_stops = go.get_all_umich_stops()
   ordering = maplib.order_by_distance(location, all_stops)

   #present X stop choices (with estimated distances)
   print """
  -------------------------
  | Stops closest to you: |
  -------------------------"""
   page_index = 0 
   user_input = "c" 
   while (user_input == "c"):
      display_results(ordering, page_index, options_per_page)
      page_index += options_per_page
      user_input = raw_input("\nSelect a stop number or press 'c' to see more stops: ")
 
   #get preferred stop
   stop_info = ordering[int(user_input)]
   preferred_stop = stop_info[2]
   preferred_stop_dist = stop_info[1]
   preferred_stop_walk_time = stop_info[0]
   print "\nLooking up route information for " + preferred_stop.names[1] + " (" + preferred_stop.names[0] + ") . . ."

   #present available bus routes
   active_routes = preferred_stop.active_routes
   print """
  ----------------------
  | Active bus routes: |
  ----------------------"""
   page_index = 0 
   user_input = "" 
   while (user_input == ""):
      i = 0
      for route in active_routes:
         print "\n [" + str(i) + "]\t" + route
         i += 1
      page_index += options_per_page
      user_input = raw_input("\nSelect one or more route numbers (e.g. 1 or 1, 2, 3): ")

   route_nums = user_input.split(',')
   route_nums = [int(x.strip()) for x in route_nums]

   #get selection(s)
   preferred_routes = [active_routes[x] for x in route_nums]

   print "\nWatching for routes! \n"

   #START BUS LIGHT SERVER
   query(preferred_stop.names[0], preferred_stop_walk_time*60, preferred_routes)

if __name__ == "__main__":
   main()
