python_requirements:
	pip install twine

test:
	python test_auto_semver.py

package:
	python setup.py sdist bdist_wheel

publish: python_requirements package
	twine upload dist/*

clean:
	rm -rf dist/ build/ __pycache__/ *.egg-info/