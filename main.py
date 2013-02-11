import go
import maplib
from get_input import *
from system_setup import *
from query import *

def main():
   options_per_page = 5

   print "Welcome to BUSL!"
   #SYSTEM SETUP
   #Set up GPIO for hardware
   #Check for network access
   if internet_on() == False:
      print "No Internet = No BUSL! \n Please Check Your Interwebs" 
      return -1      

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
   preferred_stop = ordering[int(user_input)]
   print "\nLooking up route information for " + preferred_stop[2].names[1] + " (" + preferred_stop[2].names[0] + ") . . ."

   #present available bus routes
   print """
  ----------------------
  | Active bus routes: |
  ----------------------"""
   page_index = 0 
   user_input = "c" 
   while (user_input == "c"):
      #      display_results(ordering, page_index, options_per_page)
      page_index += options_per_page
      user_input = raw_input("\nSelect a stop number or press 'c' to see more stops: ")

   #get selection(s)
   #start querying!

        #QUERYING
   #query('name',distance threshold,list of name1)
        #If within threshold, trigger event

if __name__ == "__main__":
   main()
