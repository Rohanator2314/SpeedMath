# By Rohan Shirkhedkar
import setup, time, speedmath, algebra, numguess, db, re, geometry, music, functions, login, stdiomask
from pyfiglet import Figlet
from colorama import init
init()

def game_picker():
    print("\033[1;32;40m")
    choice = int(re.sub("[^1-4]", "", input("What game would you like to play? \n1. Speed Math Basic\n2. Algebra X\n3. Geometry Galore\n4. Guess the number\nEnter number: ")) or 4)
    if choice == 1:
        speedmath.speedmath()
    elif choice == 2:
        algebra.algebra()
    elif choice == 3:
        geometry.geometry()
    elif choice == 4:
        numguess.numguess()
    else:
        print("Invalid Input")


# Prerequisites
conf_check = setup.check_config()
if conf_check is True:
    time.sleep(2)

if db.get_conf()["ONLINE"]:
    with functions.Loader("Loading Connection to Server...", "That was Fast!"):
        db.db_connect()
        time.sleep(2)
    time.sleep(1)
    functions.clear()

# Turn off Music if it is disabled
if db.get_conf()["MUSIC"] is False:
    music.done = 2

# Login
if db.get_conf()["ONLINE"]:
    login.get_connection()
    correct_login = False
    print("\033[1;31;40m")
    functions.clear()

    while not correct_login:
        login_or_register = input("\nWould you like to login or register? \n")

        if login_or_register.lower()[0] == "l":
            user = input("Username: ")
            password = stdiomask.getpass()
            correct_login = login.get_login(user, password)
        else:
            login.register()

        functions.clear()

music.start()

# Start Sequence
fig = Figlet(font="small")
print("\033[1;36;40m")
functions.clear()

print(fig.renderText("Rohanator games Presents"))
time.sleep(1.89)
functions.clear()

print(fig.renderText("A Nudgee College Production"))
time.sleep(2.53)
functions.clear()

print("\033[1;34;40m")
fig = Figlet(font="speed")
print(fig.renderText("Speed Math"))
time.sleep(0.47)
functions.clear()

print("\033[1;35;40m")
fig = Figlet(font="cricket")
print(fig.renderText("Algebra X"))
time.sleep(0.47)
functions.clear()

print("\033[1;31;40m")
fig = Figlet(font="larry3d")
print(fig.renderText("Geometry Galore"))
time.sleep(0.47)
functions.clear()

print("\033[1;32;40m")
fig = Figlet(font="chunky")
print(fig.renderText("Guess the Number!!"))
time.sleep(0.47)
functions.clear()

music.game_state = 1
print("\033[1;33;40m")
fig = Figlet(font="digital")
print(fig.renderText("Comming Soon"))
time.sleep(0.47)
functions.clear()


print("\033[1;36;40m")
fig = Figlet(font="small")
print(fig.renderText("Math Game Selector"))
time.sleep(2)


# Begin Game
try:
    game_picker()
except:
    print("\033[1;31;40m")
    print("Error, resetting...")
    time.sleep(1)
    functions.clear()

# Prevent Instant Close
while True:
    functions.clear()
    print("\033[1;31;40m")
    e = (input("Do you want to exit? (type 's' for setup)\n") or "yes")

    if e[0].lower() in ["y", "q"]:
        music.kill()
        break
    elif e[0].lower() == "s":
        setup.setup_conf()
    else:
        try:
            music.kill()
            time.sleep(0.2)
            music.start()
            game_picker()
        except:
            print("\033[1;31;40m")
            print("Error, resetting...")
            time.sleep(1)
            functions.clear()
