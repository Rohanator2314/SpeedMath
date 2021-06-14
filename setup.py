# By Rohan Shirkhedkar
import time, re
from os import path

config = {
    "USER": "D8kTAjzQVZ",
    "HOST": "remotemysql.com",
    "DATABASE": "D8kTAjzQVZ",
    "PASSWORD": "cfK7uHSzjh",
    "DIFFICULTY": 2,
    "DECIMALS": False,
    "ONLINE": True,
    "MUSIC": True,
}


def write_conf():
    global config
    try:
        file = open("config.txt", "w+")
        file.write(str(config))
    except:
        print("Error Getting Config File")


def setup_conf():
    print("\033[1;35;40m")
    print("Welcome the the config setup guide")
    print("You will be guided through the setup process" + "\n" * 3)

    global config

    # Difficulty
    print("Firstly, difficulty. 1 is easy, 2 is normal, and 3 and above is hard")
    diff = int(re.sub("[^1-4]", "", input("Which difficulty would you like to play on? \n")) or 1)
    print("\n")

    # Decimals
    print("If you enable decimals, they will activate after difficulty 4")
    decimals = (input("Would you like to play with decimals? [yes:no] \n") or "no")
    print("\n")

    # Online
    online = (input("Would you like to play online (Have access to the leaderboard)? [yes:no] \n") or "yes")
    print("\n")

    # Music
    music_setting = (input("Would you like to play with music? [yes:no] \n") or "yes")

    # Enact changes
    if diff:
        config["DIFFICULTY"] = diff

    if decimals[0].lower() == "y":
        config["DECIMALS"] = True

    if online[0].lower() == "n":
        config["ONLINE"] = False

    if music_setting[0].lower() == "n":
        config["MUSIC"] = False

    write_conf()

    print("Remember that these settings can be changed anytime by accessing the config.txt file")


def check_config():
    if path.exists("config.txt") is False:
        print("\033[1;31;40m")
        print("No config file detected...")
        print("Redirecting to config setup now...")
        time.sleep(1)
        setup_conf()
        return True
    else:
        return False
