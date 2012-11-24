all:

convert:
	echo '#!/bin/sh' > unify.sh
	cd sources && ./unify.py >> ../unify.sh
	chmod +x unify.sh
	./unify.sh
