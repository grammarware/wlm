#! /usr/bin/env python

import os, sys, glob
debug = False

mons = []

def trim(x):
	if x == 'Driekoningenpl 3a.pdf':
		return 'SOM9999'
	if x == 'Hondsberg 3.pdf':
		return 'SOM8888'
	if x[:3]!='SOM':
		print 'Unknown file name!'
		sys.exit(-1)
	c = x[3:7].strip()
	while len(c)<4:
		c = '0'+c
	return 'SOM'+c

if __name__ == '__main__':
	for x in glob.glob('*.pdf'):
		# print 'pdf2txt',"'sources/"+x+"'"
		# 		print 'mv',"'sources/"+x.replace('pdf','txt')+"'",'txt/'+trim(x)+'.txt'
		print 'git mv',"'sources/"+x+"'",'sources/'+trim(x)+'.pdf'
	for x in glob.glob('*.doc'):
		# print 'catdoc',"'sources/"+x+"'",'>','txt/'+trim(x)+'.txt'
		print 'git mv',"'sources/"+x+"'",'sources/'+trim(x)+'.doc'