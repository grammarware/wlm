#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os
import os.path
import sys
import glob
import commands
import time,datetime
import urllib, urllib2, httplib, socket
from xml.parsers.expat import ExpatError

def safelyLoadURL(url):
	errors = 0
	while errors<3:
		try:
			return urllib.urlopen(url).read()
		except IOError,e:
	 		print 'Warning: failed to load URL, retrying...'
	 		errors += 1
		except socket.error,e:
			print 'Warning: connection reset by peer, retrying...'
			errors += 1
	print 'Error fetching URL:',url
	return ''

if __name__ == "__main__":
	f = open('Antarctic1.html','w')
	f.write(safelyLoadURL('http://www.ats.aq/devPH/apa/ep_protected_search.aspx?type=1&lang=e'))
	f.close()
	for i in range(82,161)+[4,5]:
		f = open('detail%i.html' % i,'w')
		f.write(safelyLoadURL('http://www.ats.aq/devPH/apa/ep_protected_detail.aspx?type=1&id=%i&lang=e' % i))
		f.close()
	sys.exit(0)
