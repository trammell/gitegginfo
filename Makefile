usage:
	@echo "usage: make [clean|test]"

clean:
	find . -name '*.pyc' | xargs rm -f
	rm -rf gitegginfo.egg-info

test:
	python2.4 setup.py test

