# $Id:$
# $Source:$

usage:
	@echo "usage: make [clean|install]"

clean:
	find . -name '*.pyc' | xargs rm -f
	rm -rf gitegginfo.egg-info

install:


