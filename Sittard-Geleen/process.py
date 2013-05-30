#!/usr/local/bin/python

import urllib, socket

def safelyLoadURL(url):
	print '(loading %s...)' % url
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

f = open('gm.csv','r')
for line in f.readlines():
	if line.find('href=')>0:
		name = line.split("href='")[1].split("'")[0]
		g = open(name.split('/')[-1],'w')
		g.write(safelyLoadURL('http://geodata.sittard-geleen.nl/%s' % name))
		g.close()
f.close()
