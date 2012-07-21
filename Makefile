lint:
	pylint -r no yamltools

clean-pyc:
	find . -type f -name '*.pyc' -delete

release:
	python setup.py sdist upload
