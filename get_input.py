def getUserAddr():
   return raw_input("Please Enter Your Address: ")

def getUserInt(msg, max):
   while True:
      number = raw_input(msg + ": ") 
      try:
        number = int(number)
        if number >= max:
            print "Your number was out of range... Try again!"
        else:
            break
      except:
        print "You did not enter a number... Try again"


