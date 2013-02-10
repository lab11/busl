import urllib2

def internet_on():
   try:
      response=urllib2.urlopen('http://mbus.pts.umich.edu/shared/public_feed.xml',timeout=1)
      return True
   except urllib2.URLError as err: pass
   return False


