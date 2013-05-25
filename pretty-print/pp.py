#!/usr/local/bin/python

import sys

templatename = 'Tabelrij gemeentelijk monument'

if len(sys.argv)<2:
	print 'Not enough arguments!'
	sys.exit(1)
f = open(sys.argv[1],'r')
itext = f.read().split('{{'+templatename)
f.close()
otext = itext[0]
for chk in itext[1:]:
	tpl = chk.split('}}')
	tpl[0] = '\n | '.join(map(lambda x:x.replace('=',' = ').replace('  ',' ').strip(),tpl[0].split('|')))
	otext += '{{' +templatename + '\n}}'.join(tpl)
if len(sys.argv)<3:
	print otext
else:
	f = open(sys.argv[2],'w')
	f.write(otext)
	f.close()
print 'Done.'
