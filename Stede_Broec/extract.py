#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys, glob, re

keywords = ('Oorspronkelijke functie', 'Huidige functie', 'Bouwstijl', 'Bouwdatum', 'Architect')


def checkfor(s,x,v):
	if v:
		return v
	# print 'Checking "%s" for "%s".' % (s.strip(),x)
	if s.find(x)<0:
		return ''
	z = s.split(x)[1].strip()
	if z.startswith(':'):
		z = z[1:].strip()
	# print 'YES!!!:',z
	for kw in keywords:
		if z.find(kw)>-1:
			z = z.split(kw)[0]
	return z

for pdf in glob.glob('*.txt'):
	# print pdf
	obj = bj = bs = arch = adr = pc = city = monnr = kad = oof = url = ''
	f = open(pdf.replace('.txt','.pdf.src'))
	url = f.read().strip().replace('=','{{=}}')
	f.close()
	f = open(pdf)
	for line in f.readlines():
		if re.match('\d{4} [A-Z][A-Z] .*', line.strip()):
			pc = line.strip()[:7]
			city = line.strip()[7:].strip().split('    ')[0].strip()
		if line.find('Monumentnummer:')>-1:
			monnr = line.split('Monumentnummer:')[1].split()
			if len(monnr)==0:
				monnr = ''
			else:
				monnr = monnr[0].strip()
		if line.find('Adres:')>-1:
			adr = line.split('Adres:')[1].strip()
			if adr.find('Monumentnummer')>-1:
				adr = adr.split('Monumentnummer:')[0].strip()
		if line.find('Kadastraal:')>-1:
			kad = line.split('Kadastraal:')[1].strip()
			if kad.find('   ')>-1:
				kad = kad.split('   ')[0].strip()
		oof = checkfor(line,keywords[0],oof)
		obj = checkfor(line,keywords[1],obj)
		bs = checkfor(line,keywords[2],bs)
		bj = checkfor(line,keywords[3],bj)
		arch = checkfor(line,keywords[4],arch)
		if bj.find('Verbouwingen')>-1:
			bjs = bj.split('Verbouwingen')
			# print '!!!!!', (bjs[0].strip(), bjs[1].replace(':','').strip())
			if bjs[1].strip()!=':':
				bj = '%s (verbouwd in %s)' % (bjs[0].strip(), bjs[1].replace(':','').strip())
			else:
				bj = bjs[0].strip()
	f.close()
	print '''{{Tabelrij gemeentelijk monument
| object = %s
| bouwjaar = %s
| bouwstijl = %s
| architect = %s
| adres = %s
| postcode = %s
| plaats = %s
| lat = 
| lon = 
| gemcode = 0532
| objnr = %s
| MIP_nr = 
| kadaster = %s
| aangewezen = 
| oorspr_fun = %s
| url = %s
| commonscat = 
| image = 
}}''' % (obj, bj, bs, arch, adr, pc, city, monnr, kad, oof, url)
	# print ' -> Object:   "%s"' % obj
	# print ' -> bouwjaar: "%s"' % obj
	# print ' -> Address:  "%s"' % adr
	# print ' -> Monnr:    "%s"' % monnr
	# print ' -> Kadaster: "%s"' % kad
	# print ' -> Used2B:   "%s"' % oof
	# 
	#  Oorspronkelijke functie  : begraafplaats met lijkenhuisje 
	# Huidige functie    : begraafplaats met bergplaats voor gereedschap 
	# Bouwstijl      : neorenaissance bouwtrant  
	# Architect      : K. Swagerman Pz. 
	# Bouwdatum      : 1882 
	# Verbouwingen    : geen

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