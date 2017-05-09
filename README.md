# Restaurant CRUD project
Restaurant CRUD project is an application built in python for the Udacity Full Stack Nanodegree.  It focuses on creating reading updating and deleting from a database with a web interface.

This project consists of the three following files:
* database_setup.py
* lotsofmenus.py
* restaurantmenu.db
* webserver.py

## How to use
You will need to have Python and Vagrant to run on a VM.
You will also need to clone this repo, you can do so by doing the following:
```
$ git clone https://github.com/cgraffeo/restaurant-project
```
Databse is already set up.  To create a new one, you will have to delete the DB and do the following:
You will need to CD into the apropriate files, create a database running database_setup.py:
```
-> vagrant ssh
$ cd /vagrant
$ cd menu/
$ python  database_setup.py
$ python lotsofmenus.py
```
The program has been built to create a databse and populate it for you.

# Run the server:
```
$python webserver.py
```

## Web interface will be available for you on localhost:8080/restaurants