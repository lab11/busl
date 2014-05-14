BUSL
====

A pretty sweet bus light thing for magic bus

BUSL does a couple things. It will find Mbus stops close to a given location. It will find the arrival time of a route at a given stop. It will estimate your time to walk to that stop. It will display warnings at 10 minutes, 5 minutes and late (more time to walk than left before the bus arrives) represented as colors (yellow, purple and red respectively) on a Phillips Hue lightbulb or on an Arduino using Blink-M. 

Run it:
python main.py --serial <Y|N> 
The serial flag is necessary for Arduino communication

Public Mbus Feed:
http://mbus.pts.umich.edu/shared/public_feed.xml

Needs:

* A network connection.
* Elementtree
   - Download at effbot.org/downloads
   - Install with standard "sudo python setup.py install"
* pygeocoder
   - https://pypi.python.org/pypi/pygeocoder/1.2.4
* netgrowl
   - Download from the.taoofmac.com/space/projects/netgrowl
   - just a script, import it!
   - Then use the tutorial at blog.mckuhn.de/2007/10/sending-growl-notifications-from-python.html
* pyserial (for Arduino)
   - Download at pypi.python.org/pypi/pyserial
   - Install with standard "sudo python setup.py install"
* phue (for Hue)
   - https://github.com/studioimaginaire/phue
