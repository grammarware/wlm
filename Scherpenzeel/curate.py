#!/Library/Frameworks/Python.framework/Versions/3.1/bin/python3

import os, sys
debug = False

mons = []

if __name__ == '__main__':
	f = open('extracted','r')
	# g = open('curated','w')
	for line in map(lambda x:x.strip(),f.readlines()):
		byQs = line.split("'")
		if len(byQs)<6:
			print('Done')
			continue
		a,b,c = byQs[1],byQs[3],byQs[5]
		c = c.replace('\\xc2\\xb1','±').replace(' - ','–')
		if len(b)>2 and b[1] == ' ':
			b = b[0]+b[2:]
		b = b.replace('\\t',' ')
		# print(c)
		print([a,b,c])
	f.close()
	# g.close()
