
install: 
	cp reporg.py /usr/bin/orgit
	cp repotdepot.py /usr/lib/pymodules/python2.7/repotdepot.py
	cp config.ini /etc/orgit/config.ini

uninstall:
	rm /usr/bin/orgit
	rm /usr/lib/pymodules/python2.7/repotdepot.py
	rm /etc/orgit/config.ini

upgrade: uninstall install
upgrade: uninstall install

	
