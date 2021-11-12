.ONESHELL:

virtualenv:
	virtualenv .venv --python=python3

install-deps:
	pip install -r requirements.txt

format:
	black .

runserver:
	cd ./front
	npm init -y
	npm i webpack webpack-cli --save-dev
	npm install -g npm
	npm run dev
	cd ..
	pip install -i https://pypi.python.org/simple/ --upgrade -r requirements.txt
	python manage.py makemigrations
	python manage.py migrate
	python manage.py collectstatic --noinput
	python manage.py run_async_server
