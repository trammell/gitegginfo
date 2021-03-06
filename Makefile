usage:
	@echo "usage: make [clean|test]"

clean:
	sudo rm -rf build dist
	sudo rm -rf {lib,src}/*.egg-info
	rm -f readme.html
	find . -name '*.pyc' | xargs rm -f
	rm -rf build dist gitegginfo.egg-info
	rm -rf gitegginfo-*

test:
	pyflakes lib/gitegginfo/*.py
	python setup.py test

dist sdist:
	python setup.py sdist

release:
	python setup.py sdist register upload

doc readme.html:
	rst2html readme.rst readme.html

install:
	python setup.py install --force
