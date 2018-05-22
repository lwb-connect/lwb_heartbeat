# lwb_heartbeat
**Authors** : Patricia Raftery, Keith Eckert and Jay Adams
**Version**: 0.1.0


[![Coverage Status](https://coveralls.io/repos/github/lwb-connect/lwb_heartbeat/badge.svg?branch=development)](https://coveralls.io/github/lwb-connect/lwb_heartbeat?branch=development)



[![Build Status](https://travis-ci.org/lwb-connect/lwb_heartbeat.svg?branch=development)](https://travis-ci.org/lwb-connect/lwb_heartbeat.svg?branch=development)



## Overview
Love Without Boundaries is an authentic international charity that provides hope and healing to orphaned and vulnerable children, and their underserved communities, through its education, nutrition, medical, and foster care programs.  Find them at  https://www.lovewithoutboundaries.com/  This app is to automate and streamline their data input, tracking and reporting, allowing better magagement of the childrens information for. 



## Getting Started
---------------
 Create an LWB_heartbeat clone for organizing and viewing and managing the childrens information.  This app is designed to be deployed on AWS EC2 via ansible and utilizes an AWS RDS postgreSql database.   More features to come later....
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
venv
AWS EC2
AWS RDS
Ansible
Ansible playbook





## API
None at this time

## Change log
18950bb (HEAD -> jay-tues-child)  fix readme.md
d4578bc (origin/development, origin/HEAD) Merge pull request #17 from lwb-connect/jay-tues-child
9c514b8 (origin/jay-tues-child) clean up doc strings
b864d88 models edited, added relationships, remamed user app to staff, edit urls, added pillow
08c593b models edited, added relationships, remamed user app to staff, edit urls, added pillow
6dc1191 models edited, added relationships, remamed user app to staff, edit urls, added pillow
7fd00d4 Merge pull request #15 from lwb-connect/jay-tues-child
bed55c4 clean up docs in users.
0629e0d Merge pull request #14 from lwb-connect/mon-images
bcfb8de started testing, changed models, views, html
a2caba6 (jay-mon-child-two, development) Merge pull request #13 from lwb-connect/keith-monday
5712cc0 model relationhips working
8a100b2 Merge branch 'development' of https://github.com/lwb-connect/lwb_heartbeat into keith-monday
7d9c4b3 settings import to urls
79da762 Merge pull request #12 from lwb-connect/mon-images
d2ef513 Merge pull request #11 from lwb-connect/jay-mon-child
a40cf51 (origin/jay-mon-child, jay-mon-child) create child app
3a6b8a3 started form for adding photo, started view for adding and viewing photos, wrote urls
27599b8 Merge pull request #10 from lwb-connect/mon-images
e347217 fixing ansible
e3e5dd0 Merge pull request #9 from lwb-connect/jay-05-21-travis