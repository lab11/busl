import serial

def test_hardware(port):
    try:
       ser = serial.Serial(port, 9600)
       while True:
          ack = ser.readline()
          for letter in ack:
              if letter == 'R\n':
                print "Arduino RX Success"
                break
       ser.write('t\n')
       print '\t Starting hardware test...'
       count = 0;
       while True:
          print count
          ack = ser.readline()
          print ack
          if ack == 'k':
             return True
          if count >= 10000:
             print '\t Test Failed!'
             return False
          count += 1
       print '\t Test completed!'
    except:
       return False
    return True

