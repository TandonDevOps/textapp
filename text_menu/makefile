export RUN_ENV = test
REPO = text_menu
PYLINTER = flake8

FORCE:

tests: lint pytests

lint: FORCE
	flake8 *.py

pytests: FORCE
	# want to get an option for --nocapture here!
	nosetests --exe --verbose --with-coverage --cover-package=.
