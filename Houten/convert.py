#! /usr/bin/env python

import os, sys
debug = False

rcrds = []
buff = []

if __name__ == '__main__':
	f = open('Houten.wiki','r')
	# where:
	#  0 = before the list
	#  1 = inside the list
	#  2 = after the list
	where = 0
	for line in map(lambda x:x.strip(),f.readlines()):
		if where == 0:
			if line == '|----':
				where = 1
				rcrds.append([])
			print line
		elif where == 1:
			if line == '|}':
				where = 2
				buff.append(line)
			elif line == '|----':
				rcrds.append([])
			else:
				rcrds[-1].append(line[1:])
		elif where == 2:
			buff.append(line)
		else:
			print 'WTF?!'
	f.close()
	if len(rcrds[-1])==0:
		rcrds.pop()
	# print 'Got', len(rcrds), 'lines.'
	uniq = 0
	for r in rcrds:
		uniq +=1
		print '''{{Tabelrij gemeentelijk monument
| object = %s
| bouwjaar = %s
| architect = %s
| adres = %s
| postcode = 
| plaats = [[Houten]]
| lat = 
| lon = 
| gemcode = 0321
| objnr = wikinr_%i
| kadaster = 
| aangewezen = 
| oorspr_fun = %s
| image = %s
}}''' % (r[0],r[2],r[3],r[4],uniq,r[1],r[5].split(':')[1].split('|')[0])
	for line in buff:
		print line
