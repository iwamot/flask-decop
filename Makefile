.PHONY:	build
build:
	docker build -t decop .

.PHONY:	run
run:
	docker run -it --rm -p 3000:3000 -v $(CURDIR):/sample_app -e FLASK_ENV=development --name decop decop

.PHONY:	install
install:
	docker exec -it decop pip install -e .

.PHONY:	sh
sh:
	docker exec -it decop sh

.PHONY:	test
test:
	docker exec -it decop pytest

.PHONY:	coverage
coverage:
	docker exec -it decop coverage run -m pytest
	docker exec -it decop coverage report
	docker exec -it decop coverage html

.PHONY:	format
format:
	docker exec -it decop black ./
	docker exec -it decop flake8 --max-line-length=88 flask-decop app.py sample_app tests

.PHONY:	dist
dist:
	docker exec -it decop python setup.py sdist bdist_wheel

.PHONY:	uptest
uptest:	dist
	docker exec -it decop twine upload --repository-url https://test.pypi.org/legacy/ dist/*

.PHONY:	upload
upload:	dist
	docker exec -it decop twine upload dist/*
