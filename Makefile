
install: 
	cp reporg.py /usr/bin/orgit
	cp repotdepot.py /usr/lib/pymodules/python2.7/repotdepot.py

uninstall:
	rm /usr/bin/orgit
	rm /usr/lib/pymodules/python2.7/repotdepot.py

upgrade: uninstall install

