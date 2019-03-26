#Escola Aberta API
This is a [Docker][] setup for deploying your web application based on Django. It also contains tox file for testing your app.

## Requirements
You need to install [Docker][] and [Docker-Compose][].

## Production checklist
make sure your django app is configures for production use using this <a href='https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/'>link</a>.

## Build
`docker-compose build` or `make build`.

## Django models in database
`docker-compose run --rm djangoapp /bin/bash -c 'cd hello; ./manage.py makemigrations'`.

## Migrate database
`docker-compose run --rm djangoapp /bin/bash -c 'cd hello; ./manage.py migrate'`.

## Run
`docker-compose up` or `make run`.

## Tests
- `make checksafety`
- `make checkstyle`
- `make test`
- `make coverage`
