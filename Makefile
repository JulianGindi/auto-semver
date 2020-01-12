python_requirements:
	pip3 install twine

test:
	python3 test_auto_semver.py

package:
	python3 setup.py sdist bdist_wheel

publish: python_requirements package
	twine upload dist/*

clean:
	rm -rf dist/ build/ __pycache__/ *.egg-info/