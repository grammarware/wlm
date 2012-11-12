http://nl.wikipedia.org/w/index.php?title=Lijst_van_gemeentelijke_monumenten_in_Houten&oldid=33481953&action=raw
	->
		Houten.wiki

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
	Object,Oorspronkelijke functie,Bouwjaar,Architect,Adres,Afbeelding

Output:
	http://nl.wikipedia.org/wiki/Lijst_van_gemeentelijke_monumenten_in_Houten

Notes:
	- manually replace the original header with the following:
		{{Tabelkop gemeentelijke monumenten|prov-iso=nl-ge|gemeente=[[Houten]]|plaats_kop=Plaats}}