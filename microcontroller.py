import serial

def get_ports():
  import glob
  return (glob.glob("/dev/tty.usb*"))

def test_hardware(port):
       print '\t Starting hardware test...'
       ser = serial.Serial(port, 9600)
       
       # RX TEST
       count = 0
       rx_waiting = True
       while rx_waiting:
          ack = ser.readline()
          for letter in ack:
              if letter == 'R':
                print "\t Arduino RX Success"
                rx_waiting = False
          if count >= 10000:
                print '\t Test RX Timeout!'
                return False
          count += 1
 
       # TX Test
       count = 0
       tx_waiting = True
       while tx_waiting:
          ser.write('H')
          ack = ser.readline()
          for letter in ack:
            if letter == 'T':
                print "\t Arduino TX Succes"
                tx_waiting = False
          if count >= 10000:
             print '\t Test TX Timeout!'
             return False
          count += 1

       print '\t Test completed!\n'
       return True

