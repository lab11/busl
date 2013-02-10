import go
import maplib
from get_input import *
from system_setup import *

def main():
	print "Welcome to BUSL!"
	#SYSTEM SETUP
	#Set up GPIO for hardware
	#Check for network access
        if internet_on() == False:
            print "No Internet = No BUSL! \n Please Check Your Interwebs" 
 	    return -1      

	#USER CONFIG
	getUserAddr()

        #find X closest stops to user
        #present X stop choices (with estimated distances)
        #get preferred stop
        #present available bus routes
   	#get selection(s)
        #start querying!

        #QUERYING
	#Every 15 sec:
	#Get bus(es) etas for stop
        #If within threshold, trigger event

if __name__ == "__main__":
	main()
