REPO = text_menu
PYLINTER = flake8


FORCE:

tests: lint pytests

lint: FORCE
	flake8 *.py

pytests: FORCE
	nosetests --exe --verbose --with-coverage --cover-package=.

github: FORCE
	git commit -a
	git push origin main

prod: tests github
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*

dev_env: FORCE
	pip install --user -r requirements-dev.txt
