# Program

    Nazwa Programu: „MySQL configurator”
    Język Programu: Python 
    Środowisko Programistyczne: Visual Studio Code
    
    Autor programu: Łukasz Gołojuch
    
## About program

The program configures the MySQL database. Creates a database, table, etc.

## Functions

mysql_login() - function responsible for logging into the MySQL database

print_connection() - a function that displays on the screen data about the mysql account to which we are currently logged in

create_db() - function that creates a database with a user-specified name

login_db() - login to existing database

drop_db(DB_to_drop) - function removing the database from the account on which we are currently logged in

drop_table(table_to_drop) - function removing the table from the database on which we are currently logged in

## Usage

1. For the correct operation of the program, you must have MySQL services running
2. cd to folder with main.py file
3. python main.py

## Licencja
[Open Source]
