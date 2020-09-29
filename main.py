import mysql.connector
import getpass
import sys
import os

def mysql_login():
    print "-----------------------------------------------"
    #Login form to MySQL servies
    print "MySQL DB login form: \n"

    #Make all DB data global
    global host_input
    global user_input
    global password_input

    #Input data for MySQL login
    host_input = raw_input("Host: ")
    user_input = raw_input("User: ")
    password_input = getpass.getpass("Password: ")

    global mydb
    #Set db connection as global 
    mydb = mysql.connector.connect(
    host = host_input,
    user = user_input,
    password = password_input
    )
    print "\n-----------------------------------------------"

    #Check if connection was correct
    if mydb :
        print "Connection correct!"
    else:
        print "Failed to connect!"

def print_connection():
    print "You are connected to ",host_input," as ",user_input

    if 'database' in globals():
        print "Actual database:", database

def create_db():

    if not 'database' in globals():
        global database

    print "\n-----------------------------------------------"
    print "Creating new database"
    #Name of new database to be created
    database = raw_input("Name of new database: ")

    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE "+database)

    if mydb:
        print "Successful login!"
    else:
        print "Something gone wrong"

def login_db():
    
    if not 'database' in globals():
        global database
        
    print "\n-----------------------------------------------"
    print "Login to existing database: "
    database = raw_input("Name of database: ")

    mydb = mysql.connector.connect(
    host = host_input,
    user = user_input,
    password = password_input,
    database = database
    )

    if mydb:
        print "Successful login!"
    else:
        print "Something gone wrong"

def drop_db(DB_to_drop):
    #DB_to_drop - database name user would like to drop
    
    mycursor = mydb.cursor()
    #Drop database only if its exist
    mycursor.execute("DROP DATABASE IF EXISTS "+ DB_to_drop)

    database = ""

    print "Database: "+ DB_to_drop +" has been dropped!" 

def drop_table(table_to_drop):
    #table_to_drop - table name user would like to drop

    mycursor = mydb.cursor()
    #Drop database only if its exist
    sql = "DROP TABLE IF EXISTS " + table_to_drop

    mycursor.execute(sql)

    print "Table: " + table_to_drop + " has been dropped!" 

def menu():
    print "\n-----------------------------------------------"
    print_connection()
    print "\nMenu"
    print "1. Create database"
    print "2. Login to existing database"
    print "3. Drop table"
    print "4. Drop database"
    print "5. Exit"
    answ = input("\nChoice: ")

    if answ == 1:
        #Creating new database
        create_db()
        menu()
    elif answ == 2:
        #Login to existing database
        login_db()
        menu()
    elif answ == 3:
        #Drop table
        print "\n-----------------------------------------------"
        table_to_drop = input("Table you would like to drop: ")
        drop_table(table_to_drop)
        menu()
    elif answ == 4:
        #Drop database
        print "\n-----------------------------------------------"
        if 'database' in globals():
            print "Do you want to drop: "+database+" database?"
            answ = raw_input("Y/N: ")
            if answ == "y" or answ == "Y":
                drop_db(database)
            elif answ == "n" or answ == "N":
                to_drop = input("Which DB do you want to drop: ")
                drop_db(to_drop)
            else:
                main()
        else:
            to_drop = input("Which DB do you want to drop: ")
            drop_db(to_drop)     

        menu()
    elif answ == 5:
        #Exit program
        sys.exit("Thank you for using my application!")
    else:
        print "Wrong input..."
        menu()

def main():
    mysql_login()
    menu()
   
if __name__ == "__main__":
    #welcom only on first use of program
    print "\nHello", os.getlogin()
    main()
