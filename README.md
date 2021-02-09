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
