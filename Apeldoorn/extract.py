#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys, glob, re

db = []

f = open('monumentenlijst_20120117.txt', 'r')
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

f = open('monuments.txt', 'w')
# "gm# aluminiumweg 31 1 object met nr 33 Apeldoorn",
# towns = []
for e in db:
	if e.find('#')<0:
		continue
	status = e.split('#')[0]+'#'
	if status in ('k#', 'K#'):
		continue
	rest = e[len(status):].strip()
	town = addr = ''
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
	w = [status, addr, rest, town]
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