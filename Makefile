usage:
	@echo "usage: make [clean|test]"

clean:
	find . -name '*.pyc' | xargs rm -f
	rm -rf build dist gitegginfo.egg-info
	rm -rf {lib,src}/*.egg-info

test:
	pyflakes lib/gitegginfo/*.py
	python2.4 setup.py test

egg:
	python2.4 setup.py bdist_egg

