#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys, glob, re

db = []

def allnumbersof(s):
	z = s.replace(',','/').replace('-','/').split('/')
	y = []
	for x in z:
		x = x.strip()
		if re.match('[0-9]+[a-z][a-z]+',x):
			print 'WORKS'
			bx = ''
			for n in x:
				if n.isdigit():
					bx += n
				else:
					y.append(bx+n)
		else:
			y.append(x)
	print y
	return y

f = open('tampered-monumentenlijst.txt', 'r')
cur = ''
for line in f.readlines():
	if not line.strip():
		continue
	if line.split()[0][-1] == '#':
		if cur:
			db.append(cur.strip().replace('\n',' '))
		cur = line
	else:
		cur += line
f.close()
print 'Found',len(db),'entries'

ws = []
# "gm# aluminiumweg 31 1 object met nr 33 Apeldoorn",
# towns = []
for e in db:
	if e.find('#')<0:
		continue
	status = e.split('#')[0]+'#'
	if status in ('k#', 'K#'):
		continue
	rest = e[len(status):].strip()
	town = ''
	addr = []
	# TODO: '  ' -> ' '; WenumWiesel -> Wenum-Wiesel
	# town = rest.strip().split(' ')[-1]
	# if town and town.isalpha() and town[0].isupper():
	# 	if town not in towns:
	# 		towns.append(town)
	for t in ('Apeldoorn', 'Hoog Soeren', 'Uddel', 'Hoenderloo', 'Beekbergen', 'Loenen', 'Beemte  Broekland', 'Ugchelen', 'Radio  Kootwijk', 'apeldoorn', 'Klarenbeek', 'WenumWiesel', 'Lieren', 'Papegaaibeek'):
		if rest.endswith(t):
			town = t
			rest = rest[:-len(t)].strip()
			# break
	if town == '':
		if rest.startswith('Kanaal Noord'):
			town = 'Apeldoown'
		if rest.startswith('Radioweg'):
			town = 'Radio  Kootwijk'
		# print 'What is a city of',rest
		# sys.exit(1)
	obj = []
	a = False
	for word in rest.split():
		if a:
			obj.append(word)
			continue
		addr.append(word)
		if word.isdigit():
			a = not a
	#quickfix
	if len(obj)>0 and len(obj[0])==1 and obj[0].isalnum() and (len(obj)<2 or obj[1]!='object'):
		addr[-1] += obj[0]
		obj = obj[1:]
		# print 'Fixed %s and %s.' % (addr,obj)
	addr = ' '.join(addr)
	obj = ' '.join(obj)
	# met, mer, men,
	obj = obj.replace('object mer','object met').replace('object men','object met').replace('i object','1 object').replace('obj.met','object met')
	# 1 object nrs
	match = ''
	if obj.find('1 object met')>-1:
		obj,match = obj.split('1 object met')
		match = match[1:]
		obj = obj.strip()
		if obj.endswith(','):
			obj = obj[:-1]
		if match.find('.')>-1:
			ax = match.split('.')
			match = ax[0]
			obj += ' ' + '.'.join(ax[1:])
		# print '"%s" ==> "%s"' % (obj,match)
		# if obj[-5:-2] == ['1','object','met']:
		# 	print 'MATCH!'
		# print obj[-5:]
	elif obj.find('object')>0:
		print '???',obj
	w = [status, addr, obj, match, town]
	if status == 'gm#':
		ws.append(w)

# rewriting to match
fixed = False
while not fixed:
	done = False
	for w in ws:
		if done:
			# ???
			break
		if w[3]!='':
			print '     ',w
			look = w[3].lower()
			if look.startswith('nr '):
				look = look.replace('nr',' '.join(w[1].split()[:-1]))
			if look.find(' en ')>-1:
				look = look.split(' en ')[0]
			if look.startswith('nrs '):
				# default street
				s = ' '.join(w[1].split()[:-1])
				lookfor = []
				for x in allnumbersof(look[3:].strip()):
					x = x.strip()
					if x.isdigit() or len(x)<5:
						lookfor.append('%s %s' % (s,x))
					else:
						lookfor.append(x)
						s = ' '.join(x.split(' ')[:-1])
				print lookfor
				# lookfor = [look]
			else:
				lookfor = [look]
			neww = w[:]
			ws.remove(w)
			for look in lookfor:
				fnd = None
				for u in ws:
					if u[1].lower() == look:
						fnd = u
				if fnd:
					print 'Found',fnd
					if fnd[0]!=neww[0] or fnd[2]!=neww[2] or fnd[4]!=neww[4]:
						print 'Do not match, proceeding with caution'
						# sys.exit()
					ws.remove(fnd)
					neww[1] += '/' + fnd[1]
					neww[3] = ''
				else:
					print 'Not found: "%s"' % look
					# fake it till you make it!
					neww[1] += '/' + look
					neww[3] = ''
					# fixed = True
					# sys.exit()
				ws.append(neww)
				done = True
	if not done:
		fixed = True

# saving
f = open('monuments.txt', 'w')
for w in ws:
	f.write('"%s",\n' % w)
f.close()

'''
{{Tabelrij gemeentelijk monument
| object = 
| bouwjaar = 
| architect = 
| adres = 
| postcode = postcode (wordt niet getoond)
| plaats = 
| lat = 
| lon = 
| gemcode = de unieke cbs-code voor elke gemeente
| objnr = de unieke code voor het object toegend door de gemeente
| MIP_nr = het nummer van het Monumenten Inventarisatie Programma. (wordt niet getoond)
| kadaster = het kadastraal nummer (wordt niet getoond)
| aangewezen = datum dat het aagewezen is in categorie: YYYY-MM-DD (wordt niet getoond)
| oorspr_fun = het oorspronkelijke functie (boerderij, bedrijf, enz), wordt niet getoond
| url = een externe link naar een pagina met meer informatie over het monument (bij de betreffende gemeente), wordt momenteel niet getoond.
| commonscat = de categorie op Wikimedia Commons specifiek voor dit monument (als die bestaat)
| image = 
}}
'''