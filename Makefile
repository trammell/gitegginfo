usage:
	@echo "usage: make [clean|test]"

clean:
	rm -f readme.html
	find . -name '*.pyc' | xargs rm -f
	rm -rf build dist gitegginfo.egg-info
	rm -rf {lib,src}/*.egg-info

test:
	pyflakes lib/gitegginfo/*.py
	python2.4 setup.py test

egg:
	python2.4 setup.py bdist_egg

release:
	python2.4 setup.py bdist_egg register upload

doc readme.html:
	rst2html readme.rst readme.html


