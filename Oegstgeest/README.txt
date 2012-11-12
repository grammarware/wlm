http://www.oegstgeest.nl/wonen_en_burgerzaken/bouwen/lijst_gemeentelijke_monumenten_december_2010.pdf
	->
		Oegstgeest.pdf

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
	Nieuwnr,Adres,Objectaanduiding,Kadastrale Aanduiding,Postcode,Besluit tot Aanwijzing,Verzending Aanwijzing,Besluit tot Wijziging,Verzending Wijziging,Tenaamstelling

Output:
	http://nl.wikipedia.org/wiki/Lijst_van_gemeentelijke_monumenten_in_Oegstgeest

Notes:
	- 0579
	- manually replace the original header with the following:
		{{Tabelkop gemeentelijke monumenten|prov-iso=nl-ge|gemeente=[[Oegstgeest]]|plaats_kop=Plaats}}