REPO = text_menu
PYLINTER = flake8


FORCE:

tests: FORCE
	cd textapp; make tests

github: FORCE
	- git commit -a
	git push origin main

prod: tests github
	# Here we are going to package for pypi.org:
	# python3 setup.py sdist bdist_wheel
	# python3 -m twine upload dist/*

dev_env: FORCE
	pip3 install --user -r requirements-dev.txt

pkg:
	python3 -m pip install --upgrade build
	python3 -m build
	python3 -m pip install --user --upgrade twine
	python3 -m twine upload --repository pypi dist/*
