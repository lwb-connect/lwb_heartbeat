# lwb_heartbeat
**Authors** : Patricia Raftery, Keith Eckert and Jay Adams
**Version**: 0.1.0
[![Coverage Status](https://coveralls.io/repos/github/lwb-connect/lwb_heartbeat/badge.svg?branch=development)](https://coveralls.io/github/lwb-connect/lwb_heartbeat?branch=development)

[![Build Status](https://travis-ci.org/lwb-connect/lwb_heartbeat.svg?branch=development)](https://travis-ci.org/lwb-connect/lwb_heartbeat.svg?branch=development)



## Overview



## Getting Started
---------------
 Create an Imager clone for organizing and viewing artist protfolios and photos.  More features to come later....
*  Project-specific env variables
* `export SECRET_KEY='secret key'`
* `export DEBUG=True`
* `export DB_NAME=''`
* `export DB_USER=''` set these two if need for linux
* `export DB_PASSWORD=''`
* `export DB_HOST='localhost'` 

### initalize and run server

* `dropdb $DB_NAME`
* `createdb $DB_NAME`
* `./manage.py makemigrations`
* `./manage.py migrate`
* `./manage.py compilescss`
* `./manage.py collectstatic`
* `./manage.py check`
* `./manage.py test`
* `./manage.py runserver`


## Assets



## Architechture
Python 3.6
Django
bootstrap
venv
scss




## API
None at this time

## Change log
d9afbb3 finish adding scss functionality
f74ab28 added scss funtionality