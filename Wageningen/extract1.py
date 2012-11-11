#! /usr/bin/env python

import os, sys
debug = False

wrds = []

def concatable(x,y):
	if x.isdigit() and y.isdigit():
		return True
	elif x.isalpha() and y.isalpha():
		return True
	else:
		return False

if __name__ == '__main__':
	f = open('Wageningen1.txt','r')
	# monnr + straatnr
	# print '<html><body>'
	word = ''
	for x in ''.join(f.readlines()):
		if word=='':
			word = x
		else:
			if x == ' ':
				if word.strip() != '':
					wrds.append(word)
				word = ''
			elif concatable(x,word[-1]):
				word += x
			else:
				wrds.append(word)
				word = x
	f.close()
	# print 'Got',len(wrds),'wrds.'
	f = open('Wageningen2.txt','r')
	nrs=list(map(lambda x:x.strip(),f.readlines()))
	f.close()
	f = open('Wageningen3.txt','r')
	yrs=list(map(lambda x:x.strip(),f.readlines()))
	f.close()
	f = open('Wageningen4.txt','r')
	dsc=list(map(lambda x:x.strip(),f.readlines()))
	f.close()
	prev = ''
	prevbold = False
	# for word in wrds:
	monnr = [False]*len(wrds)
	for i in range(0,len(wrds)):
		word = wrds[i]
		if word.strip() == '':
			continue
		if word.isdigit() and not prev.isdigit():
			monnr[i] = True
			prevbold = True
		else:
			prevbold = False
		prev = word
	# print 'Got',len(filter(lambda x:x,monnr)),'lines from them.'
	# print 'Got',len(nrs),'numbers'
	result = []
	for i in range(0,len(wrds)):
		word = wrds[i]
		if word.strip() == '':
			continue
		if monnr[i]:
			# print '<strong>'+word+'</strong>, '
			result.append([word,'',nrs[len(result)],yrs[len(result)],dsc[len(result)]])
		elif i+1<len(monnr) and not monnr[i+1]:
			# print word+' '
			result[-1][1] +=word+' '
		else:
			# print word+', '
			result[-1][1] += word
		prev = word
	for res in result:
		# print res
		# res = [monnr,straat,huisnr,jaar,obj]
		if res[0] == '0':
			print(('{{Tabelrij gemeentelijk monument|object='+res[4]+'|bouwjaar='+res[3]+'|architect=|adres='+res[1]+' '+res[2]+'|gemcode=0289|objnr=|plaats=Wageningen|kadaster=|image=\n}}').replace('|','\n|'))
		else:
			print(('{{Tabelrij gemeentelijk monument|object='+res[4]+'|bouwjaar='+res[3]+'|architect=|adres='+res[1]+' '+res[2]+'|gemcode=0289|objnr='+res[0]+'|plaats=Wageningen|kadaster=|image=\n}}').replace('|','\n|'))
	# print '</body></html>'
	# for x in mons:
		# print x
