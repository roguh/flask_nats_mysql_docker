pyfiles = *.py tests/*.py

install-dev:
	pipenv --python 3.8
	pipenv install -r requirements.txt
	echo PLEASE RUN pipenv shell --fancy
	echo MYSQL_URL=XXX MYSQL_USER=user MYSQL_PASSWORD=password MYSQL_DATABASE=db pipenv run ./app.py

remove-dev:
	rm -f Pipfile Pipfile.lock
	pipenv --rm

up:
	docker-compose up -d --build

rebuild-app:
	docker-compose up -d --no-deps --build app

down:
	docker-compose down --remove-orphans --rmi all

run:
	docker-compose run -p 9999:9999 app sh

format:
	autopep8 --in-place --aggressive $(pyfiles)
	isort $(pyfiles)
	pydocstyle $(pyfiles)

test:
	nose2 --output-buffer --pretty-assert --log-capture --with-coverage --coverage .
