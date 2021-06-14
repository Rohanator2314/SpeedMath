# By Rohan Shirkhedkar
import time
import mysql.connector as mysql

global connection
global conf
global name


def get_conf():
    global conf
    try:
        return conf
    except:
        try:
            file = open("config.txt", "r")
            conf = eval(file.read())
            return conf
        except:
            print("Error Getting Config Data")


def db_connect():
    # Print text on initiate
    # print("Connecting to database, credentials are: \n")

    # get config data
    config = get_conf()

    try:
        # print("\033[1;30;40m")
        # print("HOST:", conf["HOST"])
        # print("DATABASE:", conf["DATABASE"])
        # print("USER:", conf["USER"])
        # print("PASSWORD:", conf["PASSWORD"] + "\n"*2)

        # connect to MySQL server
        db_connection = mysql.connect(host=config["HOST"], database=config["DATABASE"], user=config["USER"], password=config["PASSWORD"])
        # print("\033[0;37;40m")
        # print("Connected to:", db_connection.get_server_info())
        global connection
        connection = db_connection
        return db_connection
    except:
        print("\nConnection Error, if no internet is availible, turn online mode off")
        time.sleep(10)
        quit()


def give_connect():
    global connection
    return connection


def add_db(leaderboard_data, leaderboard_type):
    # Get cursor
    global connection, name
    cnx = connection
    cursor = cnx.cursor()

    # leaderboard_data = (name, score)

    print("\033[0;37;40m")

    # Required Variables
    dif = get_conf()["DIFFICULTY"]
    leaderboard = {
        1: "",
        2: "Algebra",
        3: "Geometry",
        4: "Guess",
    }

    ltype = leaderboard[leaderboard_type]
    make_leaderboard = ("CREATE TABLE IF NOT EXISTS {type}Leaderboard{num} (Player text, Score float)")
    add_leaderboard = ("INSERT INTO {type}Leaderboard{num} "
                       "(Player, Score)"
                       "VALUES (%s, %s)")
    leaderboard_print = ("SELECT Player,Score FROM `{type}Leaderboard{num}` ORDER BY Score")
    deletus = ("DELETE FROM {type}Leaderboard{num} WHERE Player=%s AND Score>%s")

    if leaderboard_type == 4:
        deletus = ("DELETE FROM {type}Leaderboard{num} WHERE Player=%s AND Score<%s")
        leaderboard_print = ("SELECT Player,Score FROM `{type}Leaderboard{num}` ORDER BY Score DESC")
        dif = ""

    # Make table if it doesnt exist
    cursor.execute(make_leaderboard.format(num=dif, type=ltype))
    time.sleep(0.5)

    # Delete worse times
    cursor.execute(deletus.format(num=dif, type=ltype), leaderboard_data)

    # Insert new leaderboard time
    cursor.execute(add_leaderboard.format(num=dif, type=ltype), leaderboard_data)

    # Make sure data is committed to the database
    cnx.commit()

    # Print Current Results
    print("Current leaderboard data for leaderboard " + str(dif) + "... \n")

    cursor.execute(leaderboard_print.format(num=dif, type=ltype))
    time.sleep(0.5)
    result = cursor.fetchall()
    c = 1
    print("Placing | Name | Time")
    for item in result:
        print(str(c) + ". ", end="")
        print(item)
        c += 1
        time.sleep(0.1)
