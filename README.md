# recipe-app-api
Python and Django rest api course - recipe app source code


## build process

```bash
vi Dockerfile
docker build .
vi docker-compose.yml
docker-compose build
docker-compose run app sh -c "django-admin.py startproject app ."
```

fails with

`Error response from daemon: unable to find user user: no matching entries in passwd file`

## travis CI

do not use due to their drop of OS Support

## flake 8

exclude Django original sources from lint due to Django using 100 chars per line

# test simple function

```
vi app/app/calc.py
vi app/app/test.py
docker-compose run app sh -c "python manage.py test"
docker-compose run app --rm sh -c "python manage.py test && flake8"
```

## TDD

 - write test first, tested code later
 - first tests will break, then they will pass

## Jenkins instead of Travis

```
docker image pull docker:dind
docker network create jenkins
docker run \
  --name jenkins-docker \
  --rm \
  --detach \
  --privileged \
  --network jenkins \
  --network-alias docker \
  --env DOCKER_TLS_CERTDIR=/certs \
  --volume jenkins-docker-certs:/certs/client \
  --volume jenkins-data:/var/jenkins_home \
  --publish 2376:2376 \
  docker:dind
docker stop jenkins-docker
```

## create core app

```
docker-compose run --rm app sh -c "python manage.py startapp core"
rm app/core/tests.py
rm app/core/views.py
mkdir app/core/tests
touch app/core/tests/__init__.py
```

add `core` to installed apps list in `app/app/settings.py`

edit `app/core/tests/test_models.py`

```
docker-compose run --rm app sh -c "python manage.py test"
```

## implement a custom user models

```
vi app/core/models.py  # add model
vi app/app/settings.py  # customize to user model
docker-compose run --rm app sh -c "python manage.py makemigrations core"  # create model User
docker-compose run --rm app sh -c "python manage.py test"  # should pass now
```

## add validation for email fields

Make invalid email raise Value Error, including test (TDD).


## add create superuser

Add test_create_new_superuser, then add create_superuser

## Now for the admin interface

First create tests
```
vi app/core/tests/test_admin.py
```

There, test own code, not django functions!

Add AdminSiteTests

get to know django url handling and creation and reverse.

learn to configure UserAdmin properties `ordering`, `list_display`, and `fieldsets`.
