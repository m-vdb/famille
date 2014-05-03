famille
=======

[![Build Status](https://travis-ci.org/m-vdb/famille.png)](https://travis-ci.org/m-vdb/famille)

A Django-based website.


Quick start
===========

Machine Dependencies
--------------------

- Install NodeJS v0.10.26: `brew install node`.
- Install virtualenv: `pip install virtualenv` or `easy_install virtualenv`.
- Install postgresql: `brew install postgresql`. You might encounter some issues with the installation of PostgreSQL, make sure your read every information from brew.
- Install foreman package: http://github.com/ddollar/foreman.

App installation
----------------

- Execute `make install`.
- Edit .env file (secret keys, database config).
- Start postgres server.
- Create a famille database in Postgres: `psql -h localhost -d postgres` and `create database famille;`.
- Load application fixtures: `./manage.py loaddata prestataires.json`.

Up and running
--------------

- Setup the database: `foreman run ./manage.py syncdb` and `foreman run ./manage.py migrate`.
- Execute `foreman run ./manage.py runserver` and access to http://localhost:8000.

Static pages (Flat pages)
-------------------------

Static pages are a good way to make content editable by user.
Some pages are required in the website. To load them (and maybe edit them),
you can perform `foreman run ./manage.py loaddata flatpages.json`