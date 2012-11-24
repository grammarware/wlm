#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
import urllib, urllib2, httplib, socket

def toInt(s):
	if s:
		return 0.0+int(s)
	else:
		return 0.0

def convertCoords(s):
	# in: 62º 01’21”S
	cs = ['']
	for i in range(0,len(s)):
		if s[i].isdigit():
			cs[-1] += s[i]
		elif cs[-1]!='':
			cs.append('')
	while len(cs)<4:
		cs.append('')
	cs[-1] = s.strip()[-1]
	# print s,cs
	r = toInt(cs[0])+(toInt(cs[1])+toInt(cs[2])/60.)/60.
	if cs[-1] in ('S','W'):
		return -r
	else:
		return r

def detag(x):
	return reduce(lambda y,a:y+a.split('<')[0],x.split('>'),'')

def getProp(xs,name):
	w = filter(lambda x:x.find(name)>0,xs)
	if not w:
		return ''
	return w[0].split('>')[1].split('<')[0]

def getDetails(n,typ):
	if typ == 'HSM':
		typ = 1
	elif typ == 'ASPA':
		typ = 2
	else:
		typ = 3
	uri = 'http://www.ats.aq/devPH/apa/ep_protected_detail.aspx?type=%i&id=%s&lang=e' % (typ,n)
	try:
		g = open('details/%s.html' % n,'r')
		details = g.readlines()
	except IOError as e:
		print '!!!! Fetching',uri
		g = open('details/%s.html' % n,'w')
		details = safelyLoadURL(uri)
		g.write(details)
	g.close()
	return uri,details

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

def extractOne(xs):
	tds = map(lambda x:detag('>'.join(x.split('>')[1:]).split('</td>')[0]).strip(),''.join(xs).split('<td'))[1:]
	if tds[0] not in ('HSM','ASMA','ASPA'):
		return []
	extra = filter(lambda x:x.find('ep_protected_detail.aspx')>0,xs)
	if extra:
		# print extra[0].split('&id=')
		j = extra[0].split('id=')[1].split('&')[0]
		# print tds,'is',j
		uri,details = getDetails(j,tds[0])
		more = \
			[
				getProp(details,'lblProponent'),
				getProp(details,'lblLatitude'),
				getProp(details,'lblLongitude'),
				getProp(details,'lblSummary'),
				getProp(details,'info_measures_listitem.aspx'),
				getProp(details,'lblManagment'),
				getProp(details,'lblAproxArea'),
				getProp(details,'lblSummary'),
				getProp(details,'info_measures_listitem.aspx'),
				getProp(details,'lnkLastReview'),
				getProp(details,'lblNextReview'),
				getProp(details,'lblAnnexV'),
				getProp(details,'lblModificationSummary'),
				getProp(details,'lblEnvironmentalDomains')
			]
	else:
		j = 0
	# print tds,j
	return [[tds[0],tds[1],tds[2]]+more+[uri]]
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
	# print 'Type;Number;Name;Proponent;Latitude;Longitude;Summary;Adopted;Management'
	print '{{Antarctic Protected Area header}}'
	for x in extracted:
		# print ';'.join(map(lambda x:x.find(';')<0 and x.strip() or repr(x),x))
		# print x
		print ('''{{Antarctic Protected Area row
| type = %s
| number = %s
| name = %s
| description = %s
| proponent = %s
| management = %s
| adopted = %s
| lat = %s
| lon = %s
| area = %s
| M_plan = %s
| alt_country1 = 
| alt_number1 = 
| commonscat = 
| url = %s
| image = 
}}''' % (x[0],x[1],x[2],x[6].strip(),x[3],x[8],x[7],convertCoords(x[4]),convertCoords(x[5]),x[9],x[16],x[-1].replace('=','{{=}}'))).replace('km2','km²')
	print '|}'
