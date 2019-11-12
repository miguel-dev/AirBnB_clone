# 0x00. AirBnB clone - The Console
## AirBnB clone project

## Description
We are building a command interpreter to manage objects. All other parts of the project will use this as a base, so it's an essential component of the project.

## How we built it:
* First, we build a parent class called BaseModel. 
* We build a flow to serialize and deserialize, Instance <-> Dictionary <-> JSON string <-> file. 
* Then all the classes for the project that inherit from BaseModel.
* First abstracted storage engine of the project: File storage.
* Create unittests to validate all classes and storage engine.

## How to use it?

Interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

Non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
