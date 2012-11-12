http://www.zaanstad.nl/sct/monumenten_archeologie/21394816/21395046/monumentenlijst/
	->
		http://www.zaanstad.nl/repositories/pdfs/sc/erfgoed_Monumenten_Zaanstad.pdf
			->
				Zaanstad.pdf

Target data model:
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
	| kadaster = het kadastraal nummer (wordt niet getoond)
	| aangewezen = datum dat het aagewezen is in categorie (wordt niet getoond)
	| oorspr_fun = het oorspronkelijke functie (boerderij, bedrijf, enz), wordt niet getoond
	| image = 
	}}
Input:
	Adres,Huisnr,Postcode,Plaats,Object,Status

Output:
	http://nl.wikipedia.org/wiki/Lijst_van_gemeentelijke_monumenten_in_Zaanstad

Notes:
	- 0479
	- manually replace the original header with the following:
		{{Tabelkop gemeentelijke monumenten|prov-iso=nl-ge|gemeente=[[Zaanstad]]|plaats_kop=Plaats}}