<p align="center">
<img src="https://img.shields.io/badge/Made%20with-Python-blue.svg"/>
<img src="https://img.shields.io/badge/SQL-blue.svg"/> 	
<img src="https://img.shields.io/badge/Markdown-black.svg"/>
</p>

---
	
# 0x02. AirBnB clone - MySQL
<div style="text-align: justify">

Thank you for visiting this repository which contain the `second step` towards building first `full web application`: the `AirBnB clone_v2`. This work starts by forking the following source: **[codebase](https://github.com/justinmajetich/AirBnB_clone.git)**
	
	
<div style="text-align: justify">
	
![hbnb](https://github.com/Alexoat76/AirBnB_clone/blob/main/assets/hbnb-logo.png?raw=true)
	
The project currently only implements the back-end `console & DBStorage`. The goal of the project is to deploy on your server a simple copy of the `AirBnB website`.

# Getting Started :running:	
<div style="text-align: justify">
	
## Table of Contents
* [About](#about)
* [Requirements](#requirements)
* [Tasks](#tasks)
* [Credits](#credits)
	
## Resources :books:

**Read or watch** :

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=AirBnB+clone+-+The+console&ei=eh8dYprkLtCawbkPs7uoCA&ved=0ahUKEwiaidyMjqP2AhVQTTABHbMdCgEQ4dUDCA4&uact=5&oq=AirBnB+clone+-+The+console&gs_lcp=Cgdnd3Mtd2l6EANKBAhBGAFKBAhGGABQAFgAYPYLaAFwAHgAgAEAiAEAkgEAmAEAwAEB&sclient=gws-wiz)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/playlist?list=PLlLHfkTcnvmPOp6jv_89tRpJUMFrP-Wbi)
	
- [cmd module](https://intranet.hbtn.io/rltoken/4nEivLRlEXGC3_ogT8S-_A) 
- **packages** concept page
- [unittest module](https://intranet.hbtn.io/rltoken/TnIpOi8cKBvpdvfqmR4Rlw) 
- [args/kwargs](https://intranet.hbtn.io/rltoken/2RJXEts8y09PKKNR4_KZaw) 
- [SQLAlchemy tutorial](https://intranet.hbtn.io/rltoken/KzB5FBMl5lh3orhpWtsNVQ) 
- [How To Create a New User and Grant Permissions in MySQL](https://intranet.hbtn.io/rltoken/9KO9mYoUjjq0A3grVHRUxw) 
- [Python3 and environment variables](https://intranet.hbtn.io/rltoken/loAjB47LzpKUqAnTnW-Ejg) 
- [SQLAlchemy](https://intranet.hbtn.io/rltoken/ra96sKNSpT0U_6h1V0tBNA) 
- [MySQL 8.0 SQL Statement Syntax](https://intranet.hbtn.io/rltoken/EbVQEW2jLkCUDXqx3TNHDQ) 
- [AirBnB clone - ORM](https://intranet.hbtn.io/rltoken/QTQdlcgZudeEa_50A57ZfQ) 	

## About
***NOTE***: 
***This part of repository is an original copy or fork of the content the initial source code to build a clone of the AirBnB website.***
	
<center> <h1>HBNB - The Console</h1> </center>

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

---
<center><h3>Original Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/justinmajetich/AirBnB_clone/blob/dev/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](https://github.com/justinmajetich/AirBnB_clone/tree/dev/tests) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/_ _init_ _.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/__init__.py) [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) [/models/place.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/place.py) [/models/city.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/city.py) [/models/amenity.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/amenity.py) [/models/state.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/state.py) [/models/review.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |<br>
<center> <h2>General Use</h2> </center>

1. First clone this repository.

3. Once the repository is cloned locate the "console.py" file and run it as follows:
```
/AirBnB_clone$ ./console.py
```
4. When this command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands
    * create - Creates an instance based on given class
    * destroy - Destroys an object based on class and UUID
    * show - Shows an object based on class and UUID
    * all - Shows all objects the program has access to, or all objects of a given class
    * update - Updates existing attributes an object based on class name and UUID
    * quit - Exits the program (EOF will as well)

##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * all - Shows all objects the program has access to, or all objects of a given class
	* count - Return number of object instances by class
    * show - Shows an object based on class and UUID
	* destroy - Destroys an object based on class and UUID
    * update - Updates existing attributes an object based on class name and UUID<br>
<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

###### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```
###### Example 3: Update an object
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 1: Destroy a User
Usage: <class_name>.destroy(<_id>)
```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 2: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 3: Update User (by dictionary)
Usage: <class_name>.update(<_id>, <dictionary>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
<br>
	
---
	
# NOTE: 
	
***In this part of repository start the work.***
	
## Background Context
Environment variables will be your best friend for this project!
*  ` HBNB_ENV ` : running environment. It can be “dev” or “test” for the moment (“production” soon!)
*  ` HBNB_MYSQL_USER ` : the username of your MySQL
*  ` HBNB_MYSQL_PWD ` : the password of your MySQL
*  ` HBNB_MYSQL_HOST ` : the hostname of your MySQL
*  ` HBNB_MYSQL_DB ` : the database name of your MySQL
*  ` HBNB_TYPE_STORAGE ` : the type of storage used. It can be “file” (using `FileStorage`) or  `db` (using `DBStorage`)

## Requirements
## General :page_with_curl:

### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs` 
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3` 
- A `README.md` file, at the root of the folder of the project, is mandatory
- The code should use the pycodestyle (version `2.8.*`)
- All files must be executable
- The length of files will be tested using `wc` 
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside a class) should have documentation 
	(`python3 -c 'print(__import__("my_module").my_function.__doc__)'` 
	and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, 
	class or method (the length of it will be verified)

### Python Unit Tests
- Allowed editors: `vi`, `vim`, `emacs` 
- All files should end with a new line
- All test files should be inside a folder `tests` 
- Use the [unittest module](https://intranet.hbtn.io/rltoken/TnIpOi8cKBvpdvfqmR4Rlw) 
- All test files should be python files (extension: `.py`)
- All test files and folders should start by `test_` 
- The file organization in the tests folder should be the same as your project: 
	ex: for `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py` 
- All tests should be executed by using this command: `python3 -m unittest discover tests` 
- Can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py` 
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside a class) should have documentation 
	(`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and 
	`python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge cases

### SQL Scripts
- Allowed editors: `vi`, `vim`, `emacs` 
- All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0` 
- Your files will be executed with `SQLAlchemy` version `1.4.x` 
- All files should end with a new line
- All SQL queries should have a comment just before (i.e. syntax above)
- All files should start by a comment describing the task
- All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc` 

## More Info
 ![](https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step2.png) 

### Comments for your SQL file:

```bash
$ cat my_script.sql
-- first 3 students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```	

## Installation :computer:
	
- Clone this repository: `git clone "https://github.com/Imanolasolo/AirBnB_clone_v2"`	
- Access AirBnb directory: `cd AirBnB_clone_v2.`
	
## Tasks

+ [x] 0\. **Fork me if you can!**

In the industry, you will work on an existing codebase 90% of the time. Your first thoughts upon looking at it might 
	include:
* “Who did this code?”
* “How it works?”
* “Where are unittests?”
* “Where is this?”
* “Why did they do that like this?”
* “I don’t understand anything.”
* “… I will refactor everything…”

But the worst thing you could possibly do is to   redo everything . Please don’t do that! **Note: the existing codebase 
might be perfect, or it might have errors. Don’t always trust the existing codebase!**

For this project you will fork this  [codebase](https://github.com/justinmajetich/AirBnB_clone.git):

* update the repository name to `AirBnB_clone_v2` 
* update the `README.md` with your information but don’t delete the initial authors.

---

+ [x] 1\. **Bug free!**

Do you remember the `unittest` module?
This codebase contains many test cases. Some are missing, but the ones included cover the basic functionality of 
	the program.

```bash
$ python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
OK
$ 
```
All the unittests  must  pass without any errors at anytime in this project,  with each storage engine! . Same for PEP8!

```bash
$ HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd 
HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db 
python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
OK
$ 
```
Some tests won’t be relevant for some type of storage, please skip them by using the *`skipIf`* feature of 
[the Unittest module - 26.3.6. Skipping tests and expected failures](https://intranet.hbtn.io/rltoken/X9E-akrXXHK17aYLxmI1zQ). 
Of course, the number of tests must be higher than the current number of tests, so if you decide to skip a test, 
you should write a new test!

### How to test with MySQL?

First, you create a specific database for it (next tasks). After, you have to remember what the purpose of an unittest?
**“Assert a current state (objects/data/database), do an action, and validate this action changed (or not) the state 
	of your objects/data/database”**

For example, “you want to validate that the `create State name="California"` command in the console will add a new 
record in your table `states` in your database”, here steps for the unittest:

* get the number of current records in the table `states` (my using a `MySQLdb` for example - but not SQLAlchemy 
	(remember, you want to test if it works, so it’s better to isolate from the system))
* execute the console command
* get (again) the number of current records in the table `states` (same method, with `MySQLdb`)
* if the difference is `+1` => test passed

---

+ [x] 2\. **Console improvements**

- **[console.py](./console.py)**
- **[models/](./models/)**
- **[tests/](./tests/)**

Update the `def do_create(self, arg):` function of your command interpreter (`console.py`) to allow for object creation 
	with given parameters:

* Command syntax: `create <Class name> <param 1> <param 2> <param 3>...` 
* Param syntax: `<key name>=<value>` 
* Value syntax:
	* String: `"<value>"` => starts with a double quote* 
		- any double quote inside the value must be escaped with a backslash `\`
	* all underscores `_` must be replace by spaces ` `. Example: You want to set the string 
	`My little house` to the attribute `name`, your command line must be `name="My_little_house"` 
	* Float: `<unit>.<decimal>` => contains a dot `.` 
	* Integer: `<number>` => default case
* If any parameter doesn’t fit with these requirements or can’t be recognized correctly by your program, 
	it must be skipped

**Don’t forget to add tests for this new feature!**

Also, this new feature will be tested here only with `FileStorage` engine.

```bash
$ cat test_params_create
create State name="California"
create State name="Arizona"
all State

create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 
max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297
all Place
$ cat test_params_create | ./console.py 
(hbnb) d80e0344-63eb-434a-b1e0-07783522124e
(hbnb) 092c9e5d-6cc0-4eec-aab9-3c1d79cfc2d7
(hbnb) [[State] (d80e0344-63eb-434a-b1e0-07783522124e) {'id': 'd80e0344-63eb-434a-b1e0-07783522124e', 
'created_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842160), 'updated_at': datetime.datetime(2017, 
11, 10, 4, 41, 7, 842235), 'name': 'California'}, [State] (092c9e5d-6cc0-4eec-aab9-3c1d79cfc2d7) {'id': 
'092c9e5d-6cc0-4eec-aab9-3c1d79cfc2d7', 'created_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842779), 
'updated_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842792), 'name': 'Arizona'}]
(hbnb) (hbnb) 76b65327-9e94-4632-b688-aaa22ab8a124
(hbnb) [[Place] (76b65327-9e94-4632-b688-aaa22ab8a124) {'number_bathrooms': 2, 'longitude': -122.431297, 
'city_id': '0001', 'user_id': '0001', 'latitude': 37.773972, 'price_by_night': 300, 'name': 
'My little house', 'id': '76b65327-9e94-4632-b688-aaa22ab8a124', 'max_guest': 10, 'number_rooms': 4, 
'updated_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 843774), 'created_at': datetime.datetime(2017, 
11, 10, 4, 41, 7, 843747)}]
(hbnb)
$
```
---

+ [x] 3\. **MySQL setup development**

+ **[setup_mysql_dev.sql](./setup_mysql_dev.sql)**

Write a script that prepares a MySQL server for the project:
* A database `hbnb_dev_db` 
* A new user `hbnb_dev` (in `localhost`)
* The password  of `hbnb_dev` should be set to `hbnb_dev_pwd` 
* `hbnb_dev` should have all privileges on the database `hbnb_dev_db` 
	(and **only this database**)
* `hbnb_dev` should have `SELECT` privilege on the database `performance_schema` 
	(and **only this database**)
* If the database `hbnb_dev_db` or the user `hbnb_dev` already exists, 
	your script should not fail

```bash
$ cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p
Enter password: 
$ echo "SHOW DATABASES;" | mysql -uhbnb_dev -p | grep hbnb_dev_db
Enter password: 
hbnb_dev_db
$ echo "SHOW GRANTS FOR 'hbnb_dev'@'localhost';" | mysql -uroot -p
Enter password: 
Grants for hbnb_dev@localhost
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost'
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost'
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost'
$ 
```
---

+ [x] 4\. **MySQL setup test**

+ **[setup_mysql_test.sql](./setup_mysql_test.sql)**

Write a script that prepares a MySQL server for the project:
* A database `hbnb_test_db` 
* A new user `hbnb_test` (in `localhost` )
* The password  of `hbnb_test` should be set to `hbnb_test_pwd` 
* `hbnb_test` should have all privileges on the database `hbnb_test_db` 
	(and **only this database**)
* `hbnb_test` should have `SELECT` privilege on the database `performance_schema` 
	(and **only this database**)
* If the database `hbnb_test_db` or the user `hbnb_test` already exists, 
	your script should not fail

```bash
$ cat setup_mysql_test.sql | mysql -hlocalhost -uroot -p
Enter password: 
$ echo "SHOW DATABASES;" | mysql -uhbnb_test -p | grep hbnb_test_db
Enter password: 
hbnb_test_db
$ echo "SHOW GRANTS FOR 'hbnb_test'@'localhost';" | mysql -uroot -p
Enter password: 
Grants for hbnb_test@localhost
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost'
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost'
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost'
$ 
```
 
+ [x] 5\. **Delete object**

+ **[file_storage.py](./models/engine/file_storage.py)**

Update `FileStorage` : (`models/engine/file_storage.py`)

* Add a new public instance method: `def delete(self, obj=None):` to delete `obj` from `__objects` 
	if it’s inside - if `obj` is equal to `None`, the method should not do anything
* Update the prototype of `def all(self)` to `def all(self, cls=None)` - that returns the list of objects 
	of one type of class. Example below with `State` - it’s an optional filtering

```bash
$ cat main_delete.py
#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.state import State

fs = FileStorage()

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create a new State
new_state = State()
new_state.name = "California"
fs.new(new_state)
fs.save()
print("New State: {}".format(new_state))

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create another State
another_state = State()
another_state.name = "Nevada"
fs.new(another_state)
fs.save()
print("Another State: {}".format(another_state))

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])        

# Delete the new State
fs.delete(new_state)

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

$ ./main_delete.py
All States: 0
New State: [State] (b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce) {'name': 'California', 
'created_at': datetime.datetime(2017, 11, 10, 1, 13, 32, 561137), 
'id': 'b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce'}
All States: 1
[State] (b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce) {'name': 'California', 
'created_at': datetime.datetime(2017, 11, 10, 1, 13, 32, 561137), 
'id': 'b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce'}
Another State: [State] (37705d25-8903-4318-9303-6d6d336a22c1) {'name': 'Nevada', 
'created_at': datetime.datetime(2017, 11, 10, 1, 13, 34, 619133), 
'id': '37705d25-8903-4318-9303-6d6d336a22c1'}
All States: 2
[State] (b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce) {'name': 'California', 
'created_at': datetime.datetime(2017, 11, 10, 1, 13, 32, 561137), 
'id': 'b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce'}
[State] (37705d25-8903-4318-9303-6d6d336a22c1) {'name': 'Nevada', 
'created_at': datetime.datetime(2017, 11, 10, 1, 13, 34, 619133), 
'id': '37705d25-8903-4318-9303-6d6d336a22c1'}
All States: 1
[State] (37705d25-8903-4318-9303-6d6d336a22c1) {'name': 'Nevada', 
'created_at': datetime.datetime(2017, 11, 10, 1, 13, 34, 619133), 
'id': '37705d25-8903-4318-9303-6d6d336a22c1'}
$ 
```
---

+ [x] 6\. **DBStorage - States and Cities**

- **[base_model.py](./models/base_model.py)**
- **[city.py](./models/city.py)**
- **[state.py](./models/state.py)**
- **[db_storage.py](./models/engine/db_storage.py)**
- **[__init__.py](./models/__init__.py)**

**State creation**:

```bash
$ echo 'create State name="California"' | HBNB_MYSQL_USER=hbnb_dev 
HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db 
HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) 95a5abab-aa65-4861-9bc6-1da4a36069aa
(hbnb)
$ 
$ echo 'all State' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd 
HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[State] (95a5abab-aa65-4861-9bc6-1da4a36069aa) {'name': 'California', 
'id': '95a5abab-aa65-4861-9bc6-1da4a36069aa', 'updated_at': 
datetime.datetime(2017, 11, 10, 0, 49, 54), 'created_at': datetime.datetime(2017, 11, 10, 0, 49, 54)}]
(hbnb)
$ 
$ echo 'SELECT * FROM states\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
created_at: 2017-11-10 00:49:54
updated_at: 2017-11-10 00:49:54
      name: California
$ 
```

**City creation**:

```bash
$ echo 'create City state_id="95a5abab-aa65-4861-9bc6-1da4a36069aa" name="San_Francisco"' | 
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost 
HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
(hbnb) 4b457e66-c7c8-4f63-910f-fd91c3b7140b
(hbnb)
$ 
$ echo 'all City' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd 
HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[City] (4b457e66-c7c8-4f63-910f-fd91c3b7140b) {'id': '4b457e66-c7c8-4f63-910f-fd91c3b7140b', 
'updated_at': datetime.datetime(2017, 11, 10, 0, 52, 53), 'state_id': '95a5abab-aa65-4861-9bc6-1da4a36069aa', 
'name': 'San Francisco', 'created_at': datetime.datetime(2017, 11, 10, 0, 52, 53)]
(hbnb)
$ 
```

```bash
$ echo 'create City state_id="95a5abab-aa65-4861-9bc6-1da4a36069aa" name="San_Jose"' | 
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost 
HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
(hbnb) a7db3cdc-30e0-4d80-ad8c-679fe45343ba
(hbnb)
$ 
$ echo 'SELECT * FROM cities\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 4b457e66-c7c8-4f63-910f-fd91c3b7140b
created_at: 2017-11-10 00:52:53
updated_at: 2017-11-10 00:52:53
      name: San Francisco
  state_id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
*************************** 2. row ***************************
        id: a7db3cdc-30e0-4d80-ad8c-679fe45343ba
created_at: 2017-11-10 00:53:19
updated_at: 2017-11-10 00:53:19
      name: San Jose
  state_id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
$ 
```
---

+ [x] 7\. **DBStorage - User**

+ **[user.py](./models/user.py)**

```bash
$ echo 'create User email="gui@hbtn.io" password="guipwd" first_name="Guillaume" 
last_name="Snow"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost 
HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) 4f3f4b42-a4c3-4c20-a492-efff10d00c0b
(hbnb) 
$
$ echo 'all User' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost 
HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[User] (4f3f4b42-a4c3-4c20-a492-efff10d00c0b) {'updated_at': 
datetime.datetime(2017, 11, 10, 1, 17, 26), 'id': '4f3f4b42-a4c3-4c20-a492-efff10d00c0b', 
'last_name': 'Snow', 'first_name': 'Guillaume', 'email': 'gui@hbtn.io', 'created_at': 
datetime.datetime(2017, 11, 10, 1, 17, 26), 'password': 'f4ce007d8e84e0910fbdd7a06fa1692d'}]
(hbnb) 
$
$ echo 'SELECT * FROM users\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 4f3f4b42-a4c3-4c20-a492-efff10d00c0b
created_at: 2017-11-10 01:17:26
updated_at: 2017-11-10 01:17:26
     email: gui@hbtn.io
  password: guipwd
first_name: Guillaume
 last_name: Snow
$
```
---

+ [x] 8\. **DBStorage - Place**

- **[place.py](./models/place.py)**
- **[user.py](./models/user.py)**
- **[city.py](./models/city.py)**

```bash
$ echo 'create Place city_id="4b457e66-c7c8-4f63-910f-fd91c3b7140b" user_id="4f3f4b42-a4c3-4c20-a492-efff10d00c0b" 
name="Lovely_place" number_rooms=3 number_bathrooms=1 max_guest=6 price_by_night=120 latitude=37.773972 
longitude=-122.431297' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost 
HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) ed72aa02-3286-4891-acbc-9d9fc80a1103
(hbnb) 
$ 
$ echo 'all Place' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost 
HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[Place] (ed72aa02-3286-4891-acbc-9d9fc80a1103) {'latitude': 37.774, 'city_id': '4b457e66-c7c8-4f63-910f-fd91c3b7140b', 
'price_by_night': 120, 'id': 'ed72aa02-3286-4891-acbc-9d9fc80a1103', 'user_id': '4f3f4b42-a4c3-4c20-a492-efff10d00c0b', 
'max_guest': 6, 'created_at': datetime.datetime(2017, 11, 10, 1, 22, 30), 'description': None, 'number_rooms': 3, 
'longitude': -122.431, 'number_bathrooms': 1, 'name': '"Lovely place', 'updated_at': datetime.datetime(2017, 11, 10, 1, 22, 30)}]
(hbnb) 
$ 
$ echo 'SELECT * FROM places\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
              id: ed72aa02-3286-4891-acbc-9d9fc80a1103
      created_at: 2017-11-10 01:22:30
      updated_at: 2017-11-10 01:22:30
         city_id: 4b457e66-c7c8-4f63-910f-fd91c3b7140b
         user_id: 4f3f4b42-a4c3-4c20-a492-efff10d00c0b
            name: "Lovely place"
     description: NULL
    number_rooms: 3
number_bathrooms: 1
       max_guest: 6
  price_by_night: 120
        latitude: 37.774
       longitude: -122.431
$ 
```
---
 
+ [x] 9\. **DBStorage - Review**

- **[review.py](./models/review.py)**
- **[user.py](./models/user.py)**
- **[place.py](./models/place.py)**

```bash
$ 
$ echo 'create User email="bob@hbtn.io" password="bobpwd" first_name="Bob" last_name="Dylan"' | 
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db 
HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) d93638d9-8233-4124-8f4e-17786592908b
(hbnb) 
$ 
$ echo 'create Review place_id="ed72aa02-3286-4891-acbc-9d9fc80a1103" 
user_id="d93638d9-8233-4124-8f4e-17786592908b" text="Amazing_place,_huge_kitchen"' | HBNB_MYSQL_USER=hbnb_dev 
HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db 
./console.py 
(hbnb) a2d163d3-1982-48ab-a06b-9dc71e68a791
(hbnb) 
$ 
$ echo 'all Review' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd 
HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[Review] (f2616ff2-f723-4d67-85dc-f050a38e0f2f) {'text': 'Amazing place, huge kitchen', 
'place_id': 'ed72aa02-3286-4891-acbc-9d9fc80a1103', 'id': 'f2616ff2-f723-4d67-85dc-f050a38e0f2f', 
'updated_at': datetime.datetime(2017, 11, 10, 4, 6, 25), 'created_at': datetime.datetime(2017, 11, 10, 4, 6, 25), 
'user_id': 'd93638d9-8233-4124-8f4e-17786592908b'}]
(hbnb) 
$ 
$ echo 'SELECT * FROM reviews\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: f2616ff2-f723-4d67-85dc-f050a38e0f2f
created_at: 2017-11-10 04:06:25
updated_at: 2017-11-10 04:06:25
      text: Amazing place, huge kitchen
  place_id: ed72aa02-3286-4891-acbc-9d9fc80a1103
   user_id: d93638d9-8233-4124-8f4e-17786592908b
$ 
```
---

+ [x] 10\. **DBStorage - Amenity... and BOOM!**

- **[amenity.py](./models/amenity.py)**
- **[place.py](./models/place.py)**
 
```bash
$ cat main_place_amenities.py 
#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models import *

# creation of a State
state = State(name="California")
state.save()

# creation of a City
city = City(state_id=state.id, name="San Francisco")
city.save()

# creation of a User
user = User(email="john@snow.com", password="johnpwd")
user.save()

# creation of 2 Places
place_1 = Place(user_id=user.id, city_id=city.id, name="House 1")
place_1.save()
place_2 = Place(user_id=user.id, city_id=city.id, name="House 2")
place_2.save()

# creation of 3 various Amenity
amenity_1 = Amenity(name="Wifi")
amenity_1.save()
amenity_2 = Amenity(name="Cable")
amenity_2.save()
amenity_3 = Amenity(name="Oven")
amenity_3.save()

# link place_1 with 2 amenities
place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)

# link place_2 with 3 amenities
place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)

storage.save()

print("OK")

$ 
$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost 
HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./main_place_amenities.py
OK
$ 
$ echo 'SELECT * FROM amenities\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 47321eb8-152a-46df-969a-440aa67a6d59
created_at: 2017-11-10 04:22:02
updated_at: 2017-11-10 04:22:02
      name: Cable
*************************** 2. row ***************************
        id: 4a307e7f-68f9-438f-81c0-8325898dda2a
created_at: 2017-11-10 04:22:02
updated_at: 2017-11-10 04:22:02
      name: Oven
*************************** 3. row ***************************
        id: b80aec52-d0c9-420a-8471-3254572954b6
created_at: 2017-11-10 04:22:02
updated_at: 2017-11-10 04:22:02
      name: Wifi
$ 
$ echo 'SELECT * FROM places\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
              id: 497e3867-d6e9-4401-9c7c-9687c18d2ac7
      created_at: 2017-11-10 04:22:02
      updated_at: 2017-11-10 04:22:02
         city_id: 9d60df6e-31f7-430c-8162-69e89f4a17aa
         user_id: 9b37bd51-6aef-485f-bf10-c7ab83fea2e9
            name: House 1
     description: NULL
    number_rooms: 0
number_bathrooms: 0
       max_guest: 0
  price_by_night: 0
        latitude: NULL
       longitude: NULL
*************************** 2. row ***************************
              id: db549ae1-4500-4d0c-9b50-4b4978ed229e
      created_at: 2017-11-10 04:22:02
      updated_at: 2017-11-10 04:22:02
         city_id: 9d60df6e-31f7-430c-8162-69e89f4a17aa
         user_id: 9b37bd51-6aef-485f-bf10-c7ab83fea2e9
            name: House 2
     description: NULL
    number_rooms: 0
number_bathrooms: 0
       max_guest: 0
  price_by_night: 0
        latitude: NULL
       longitude: NULL
$ 
$ echo 'SELECT * FROM place_amenity\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
  place_id: 497e3867-d6e9-4401-9c7c-9687c18d2ac7
amenity_id: 47321eb8-152a-46df-969a-440aa67a6d59
*************************** 2. row ***************************
  place_id: db549ae1-4500-4d0c-9b50-4b4978ed229e
amenity_id: 47321eb8-152a-46df-969a-440aa67a6d59
*************************** 3. row ***************************
  place_id: db549ae1-4500-4d0c-9b50-4b4978ed229e
amenity_id: 4a307e7f-68f9-438f-81c0-8325898dda2a
*************************** 4. row ***************************
  place_id: 497e3867-d6e9-4401-9c7c-9687c18d2ac7
amenity_id: b80aec52-d0c9-420a-8471-3254572954b6
*************************** 5. row ***************************
  place_id: db549ae1-4500-4d0c-9b50-4b4978ed229e
amenity_id: b80aec52-d0c9-420a-8471-3254572954b6
$ 
```
---

## Credits

## Author(s):blue_book:

Work is owned and maintained by 
	**`Imanol Asolo`**  and **`Alex Arévalo`**.

<3848@holbertonschool.com>

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/25px-Octicons-mark-github.svg.png)](https://github.com/Imanolasolo)
[![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/25px-Twitter_Bird.svg.png)](https://twitter.com/jjusturi)
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/25px-LinkedIn_logo_initials.png)](https://www.linkedin.com/in/imanol-asolo-5ba9b42a/)

<3915@holbertonschool.com>
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/25px-Octicons-mark-github.svg.png)](https://github.com/Alexoat76)
[![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/25px-Twitter_Bird.svg.png)](https://twitter.com/aoarevalot)
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/25px-LinkedIn_logo_initials.png)](https://www.linkedin.com/in/Alexoat76/)

## Acknowledgments :mega: 

### **`Holberton School`** (*providing guidance*)
	
This program was written as part of the curriculum for Holberton School.
Holberton School is a campus-based full-stack software engineering program
that prepares students for careers in the tech industry using project-based
peer learning. For more information,  please visit [this link](https://www.holbertonschool.com/).
![Brand](https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg)
