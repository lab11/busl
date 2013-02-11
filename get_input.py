def get_user_addr():
   return raw_input("Please enter your location or an address: ")

def get_user_int(msg, max):
   number = -1
   while True:
      number = raw_input(msg) 
      try:
        number = int(number)
        if number >= max and max != -1:
            print "Your number was out of range... Try again!"
        else:
            break
      except:
        print "You did not enter a number... Try again"
   return number

def display_results(ordering, start_index, n): 
   closest = ordering[start_index:start_index+n]
   option = start_index
   for s in closest:
      print("\n [" + str(option) + "]\t"  + s[2].names[1] + " (" + s[2].names[0] + ") " + 
      "\n\tDist: " + str(int(s[1])+1) + " meters" +
      "\n\tApprox. walking time: " + str(int(s[0])+1) + " mins")
      option += 1

def display_serial_ports(start_index):
   import glob
   results = (glob.glob("/dev/tty.usb*"))
   option = start_index
   for port in results:
     print "\n [" + str(option) + "]\t" + port
     option += 1
   return results
