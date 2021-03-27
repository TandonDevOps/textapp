REPO = text_menu
PYLINTER = flake8


FORCE:

tests: FORCE
	cd text_menu; make tests

github: FORCE
	- git commit -a
	git push origin main

prod: tests github
	# python3 setup.py sdist bdist_wheel
	# python3 -m twine upload dist/*

dev_env: FORCE
	pip3 install --user -r requirements-dev.txt
