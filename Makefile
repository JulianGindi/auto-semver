python_requirements:
	pip3 install twine

package:
	python3 setup.py sdist bdist_wheel

publish: python_requirements package
	twine upload dist/*

clean:
	rm -rf dist/ __pycache__/ *.egg-info/