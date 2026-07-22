REPO = text_menu
PYLINTER = flake8


FORCE:

tests: FORCE
	cd textapp; make tests

github: FORCE
	- git commit -a
	git push origin main

prod: tests github pkg

dev_env: FORCE
	pip3 install -r requirements-dev.txt

pkg: setup_pkg upload_pkg

setup_pkg:
	# we need to fix bump_version.sh!
	python3 setup.py sdist bdist_wheel
	python3 -m pip install --upgrade build
	python3 -m build
	python3 -m pip install --upgrade twine

upload_pkg:
	python3 -m twine upload --verbose --repository pypi --repository-url https://upload.pypi.org/legacy/ dist/*
