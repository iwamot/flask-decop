.PHONY:	build
build:
	docker build -t skinny .

.PHONY:	run
run:
	docker run -it --rm -p 3000:3000 -v $(CURDIR):/sample_app -e FLASK_ENV=development --name skinny skinny

.PHONY:	install
install:
	docker exec -it skinny pip install -e .

.PHONY:	sh
sh:
	docker exec -it skinny sh

.PHONY:	test
test:
	docker exec -it skinny pytest

.PHONY:	coverage
coverage:
	docker exec -it skinny coverage run -m pytest
	docker exec -it skinny coverage report
	docker exec -it skinny coverage html

.PHONY:	format
format:
	docker exec -it skinny black ./
	docker exec -it skinny flake8 --max-line-length=88 flask-skinny app.py sample_app tests

.PHONY:	dist
dist:
	docker exec -it skinny python setup.py sdist bdist_wheel

.PHONY:	uptest
uptest:	dist
	docker exec -it skinny twine upload --repository-url https://test.pypi.org/legacy/ dist/*

.PHONY:	upload
upload:	dist
	docker exec -it skinny twine upload dist/*
