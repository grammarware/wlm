http://geodata.sittard-geleen.nl/monumenten.html?ondergrond=2&kml=static%2Fmonumenten%2Fstadsgezichten.kml
	->
		http://geodata.sittard-geleen.nl/static/monumenten/gm.csv
			->
				http://geodata.sittard-geleen.nl/static/monumenten/pdfs/*.pdf

Target data model:
	{{Tabelrij gemeentelijk monument
	| object = %s
	| adres = %s
	| plaats = %s
	| gemcode = 1883
	| objnr = wikinr_%i
	}}

Input:
	PDF :(

Output:
	http://nl.wikipedia.org/wiki/Lijst_van_gemeentelijke_monumenten_in_Sittard-Geleen
