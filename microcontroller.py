import serial, time

ser = ''

def get_ports():
  import glob
  return (glob.glob("/dev/tty.usb*"))

def beat():
   ser.write('B')

def tx2(msg): 
   ser.write(msg)

def tx(msg):
  count = 0
  tx_waiting = True
  while tx_waiting:
      ser.write(msg)
      ack = ser.readline()
      for letter in ack:
          if letter == 'T':
             print "\t Sent " + msg
             tx_waiting = False
      if count >= 1000:
             print '\t Test TX Timeout!'
             return False
      count += 1
  return True
   
def fire(type):
  if type == "red":
     print "\t Firing RED"
     tx('r')
  if type == "orange":
     print "\t Firing ORANGE"
     tx('o')
  if type == "cyan":
     print "\t Firing CYAN"
     tx('c')
  if type == "off":
     print "\t Firing OFF"
     tx('x')
  print "\t Done Firing"
  return
 
def rx(msg):
   count = 0
   rx_waiting = True
   while rx_waiting:
       ack = ser.readline()
       for letter in ack:
          if letter == msg:
            print "\t Recieved " + letter
            rx_waiting = False
       if count >= 10000:
            print '\t Test RX Timeout!'
            return False
       count += 1
   return True

def test_hardware(port):
       global ser 
       ser = serial.Serial(port, 9600)
       
       print '\n\t Starting hardware test...'
       if rx('R'):
          print "\t Arduino RX Success"
       else:
          print "Hardware RX failed!"
          return False
       if tx('H'):
          print "\t Arduino TX Success"
       else:
          print "Hardware TX failed!"
          return False
       print '\t Test completed!\n'
       return True

