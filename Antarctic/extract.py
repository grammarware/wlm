#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys

def detag(x):
	return reduce(lambda y,a:y+a.split('<')[0],x.split('>'),'')

def getProp(xs,name):
	w = filter(lambda x:x.find(name)>0,xs)
	if not w:
		return ''
	return w[0].split('>')[1].split('<')[0]

def extractOne(xs):
	tds = map(lambda x:detag('>'.join(x.split('>')[1:]).split('</td>')[0]).strip(),''.join(xs).split('<td'))[1:]
	if tds[0]!='HSM':
		return []
	extra = filter(lambda x:x.find('ep_protected_detail.aspx')>0,xs)
	if extra:
		# print extra[0].split('&id=')
		j = extra[0].split('id=')[1].split('&')[0]
		g = open('detail%s.html' % j,'r')
		details = g.readlines()
		more = \
			[
				getProp(details,'lblProponent'),
				getProp(details,'lblLatitude'),
				getProp(details,'lblLongitude'),
				getProp(details,'lblSummary'),
				getProp(details,'info_measures_listitem.aspx'),
				getProp(details,'lblManagment')
			]
		# filter(lambda x:x.find('lblLatitude')>0,details)
		g.close()
	else:
		j = 0
	# print tds,j
	return [[tds[0],tds[1],tds[2]]+more]
	# sys.exit(1)
	
if __name__ == "__main__":
	extracted = []
	for n in range(1,5):
		f = open('Antarctic%i.html' % n,'r')
		lines = map(lambda x:x.strip(),f.readlines())
		for i in range(0,len(lines)):
			if lines[i].find('tablainfo_interior')<0:
				continue
			j = i+1
			while(lines[j].find('</tr>')<0): j += 1
			extracted.extend(extractOne(lines[i:j]))
			i = j+1
		f.close()
	print 'Type;Number;Name;Proponent;Latitude;Longitude;Summary;Adopted;Management'
	for x in extracted:
		print ';'.join(map(lambda x:x.find(';')<0 and x.strip() or repr(x),x))
