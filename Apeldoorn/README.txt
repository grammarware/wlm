http://www.apeldoorn.nl/DATA/TER/docs/bezoek/cultuurhistorie/monumenten/monumentenlijst_20120117.pdf
	->
		monumentenlijst_20120117.txt
			->
				tampered-monumentenlijst.txt

Target data model:
	{{Tabelrij gemeentelijk monument
	| object = %s
	| adres = %s
	| plaats = %s
	| gemcode = 0200
	| objnr = wikinr_%i
	| url = http://www.apeldoorn.nl/DATA/TER/docs/bezoek/cultuurhistorie/monumenten/monumentenlijst_20120117.pdf
	}}
Input:
	Status, Street, House Number, House Letter, andui, Toev., Kind of object, Specials, City

Output:
	http://nl.wikipedia.org/wiki/Lijst_van_gemeentelijke_monumenten_in_Apeldoorn

Notes:
	- some manual fixes…
	- header:
			{{Tabelkop gemeentelijke monumenten|prov-iso=nl-ge|gemeente=[[Apeldoorn]]|plaats_kop=Plaats}}
