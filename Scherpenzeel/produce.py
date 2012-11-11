#!/Library/Frameworks/Python.framework/Versions/3.1/bin/python3

import os, sys
debug = False

mons = []

if __name__ == '__main__':
	f = open('curated','r')
	for line in map(lambda x:x.strip(),f.readlines()):
		byQs = line.split("'")
		if len(byQs)<6:
			# print('Done')
			continue
		a,b,c = byQs[1],byQs[3],byQs[5]
		# {{Tabelrij gemeentelijk monument|object={{sorteer|Christelijke HBS|Vm. Christelijke HBS}}<br/>(Augustinuscollege)|bouwjaar={{sorteer|1955|1955-'57}}|architect={{sorteer|Offringa 1955|[[Rienk Offringa|R. Offringa]]}}<br/>[[Derk Broos|D. Broos]]|adres={{sorteer|Admiraal de Ruyterlaan 37|Admiraal de Ruyterlaan 37-39}}|gemcode=0014|objnr=104509|image=}}
		# print([a,b,c])
		print(('{{Tabelrij gemeentelijk monument|object='+b+'|bouwjaar='+c+'|architect=|adres='+a+'|gemcode=0279|objnr=|plaats=Scherpenzeel|kadaster=|image=\n}}').replace('|','\n|'))
	f.close()
