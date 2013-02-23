#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
import urllib, urllib2, httplib, socket

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
	root = 'http://www.stedebroec.nl'
	for line in safelyLoadURL(root+'/Vrije-tijd-en-toerisme/Gemeentelijke-Monumenten.htm').split('\n'):
		if line.find('web/file')>0:
			lnk = line.split('"')[3]
			if lnk.startswith('/web/file'):
				url = root+lnk.replace('&amp;','&')
				fn = line.split('title="')[1].split('"')[0]
				f = open(fn+'.src','w')
				f.write(url)
				f.close()
				f = open(fn,'w')
				f.write(safelyLoadURL(url))
				f.close()
