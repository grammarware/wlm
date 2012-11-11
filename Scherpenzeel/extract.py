#! /usr/bin/env python

import os, sys
debug = False

mons = []

if __name__ == '__main__':
	f = open('Scherpenzeel.txt','r')
	where = 0
	# 0 = shit
	# 1 = Perceeladres
	# 2 = Omschrijving
	# 3 = Bouwjaar
	for line in map(lambda x:x.strip(),f.readlines()):
		if debug:
			print 'Read "'+line+'"',where
		if where == 0:
			if line == 'Perceeladres' or line == 'Perceelsadres':
				where = 1
				cx = cx2 = 0
			else:
				if debug:
					print 'Skip "'+line+'"'
			continue
		elif where == 1:
			if line == 'Omschrijving':
				where = 2
				cx2 = cx
			else:
				mons.append([line,'',''])
				if debug:
					print 'Addd "'+line+'"'
				cx += 1
		elif where == 2:
			if line == 'Bouwjaar':
				where = 3
			elif cx2 < 1:
				print 'WTF too much descs'
				where = 3
			else:
				mons[-cx2][1] = line
				cx2 -= 1
		elif where == 3:
			if debug:
				print '????',where,cx
			if cx == 1:
				where = 0
			else:
				mons[-cx][2] = line
				cx -= 1
		else:
			print 'WTF'
	f.close()
	print 'Got',len(mons),'mons'
	for x in mons:
		print x
