from phue import Bridge
import random,sys,time

def set_white(light):
  light.brightness = 150
  light.xy = [0,0]

def ack(light):
  light.brightness = 150
  light.xy = [0,0]
  light.on = False
  time.sleep(1)
  light.on = True

def set_purple(light):
  light.brightness = 150
  light.xy = [.3,.2];

def set_red(light):
  light.brightness = 150
  light.xy = [.75,.3];

def set_yellow(light):
  light.brightness = 127
  light.xy = [1,1]

def hue_connect():
  bridge = Bridge('4908hue')
  bridge.connect()
  all_lights = bridge.get_light_objects()
  return all_lights

#lights = hue_connect()
#ack(lights[1])
#set_yellow(lights[1])
