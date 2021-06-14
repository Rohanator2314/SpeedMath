import mysql.connector.errors

import db, time, stdiomask, re

global connection


def get_connection():
    global connection
    connection = db.give_connect()


def check_exists(user, password):
    # Get cursor
    global connection
    cnx = connection
    cursor = cnx.cursor()

    get_exists = ("SELECT * FROM `Login` WHERE User='{user}' AND Pass='{password}'")

    try:
        cursor.execute(get_exists.format(user=user, password=password))
        time.sleep(0.5)
    except mysql.connector.errors.ProgrammingError:
        print("Invalid Username or Password")

    data = "error"  # initially just assign the value

    for i in cursor:
        data = i  # if cursor has no data then loop will not run and value of data will be 'error'

    if data == "error":
        return False
    else:
        return True


def get_login(user, password):
    exists = check_exists(user, password)

    if exists is False:
        print("Incorrect username or password")

    return exists


def register():
    # Get cursor
    global connection
    cnx = connection
    cursor = cnx.cursor()

    user = input("Desired Username: ")
    password = stdiomask.getpass("Desired Password: ")
    password2 = stdiomask.getpass("Confirm Password: ")

    register_code = ("INSERT INTO `Login`(`User`, `Pass`) VALUES ('{user}','{password}')")

    if password == password2 and check_exists(user, password) is False:
        try:
            cursor.execute(register_code.format(user=user, password=password))
            time.sleep(0.5)

            # Make sure data is committed to the database
            cnx.commit()

            print("Success!")

        except mysql.connector.errors.ProgrammingError:
            print("Invalid Username or Password")

    elif password != password2:
        print("Passwords don't match")

    else:
        print("Credentials already exist")

    time.sleep(1.2)
