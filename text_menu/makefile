REPO = text_menu
PYLINTER = flake8

FORCE:

tests: lint pytests

lint: FORCE
	flake8 *.py

pytests: FORCE
	nosetests --exe --verbose --with-coverage --cover-package=.
