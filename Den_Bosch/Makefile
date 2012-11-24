all:

unify:
	echo '#!/bin/sh' > unify.sh
	cd sources && ./unify.py >> ../unify.sh
	chmod +x unify.sh
	./unify.sh

convert:
	rm -f text/*.txt
	ls -1 sources/*.pdf | xargs -n1 pdf2txt
	mv sources/*.txt text/

convertdoc:
	ls -1 sources/*.doc | xargs -n1 ./doc2txt
