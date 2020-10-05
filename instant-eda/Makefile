.PHONY: docs examples

docs:
	rm -rf docs/
	mkdir docs/
	# pdoc3
	cp -a ./docsrc/assets/ ./docs/assets/
	pdoc3 --html --force --output-dir docs instant_eda
	mv docs/instant_eda/* docs
	rmdir docs/instant_eda
	# sphinx
	cd docsrc/ && make github

test:
	pytest --black tests/unit/
	pytest --black tests/issues/
	pytest --nbval tests/notebooks/
	flake8 . --select=E9,F63,F7,F82 --show-source --statistics

pypi_package:
	make install
	check-manifest
	python setup.py sdist bdist_wheel
	twine check dist/*
	twine upload --skip-existing dist/*

install:
	pip install -e .[notebook,app]

lint:
	isort --profile black .
	black .

typing:
	pytest --mypy -m mypy .

clean:
	git rm --cached `git ls-files -i --exclude-from=.gitignore`

all:
	make lint
	make install
	make examples
	make docs
	make test
	make typing
