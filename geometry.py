import db, time, random, music, functions
from pyfiglet import Figlet
from turtle import *
from time import perf_counter as count

mark = 0


def lb(name, score):
    # Add leaderboard Entry
    leaderboard_data = (name, score)
    db.add_db(leaderboard_data, 3)


def questions(i, turtle, text):
    global mark

    print("\033[1;32;40m")
    # Variables
    len = db.get_conf()["DIFFICULTY"] * 6
    xlen = random.randint(1, len) * 25
    ylen = random.randint(1, len) * 25
    measure_type = random.randint(1, 2)
    measure = {
        1: "area",
        2: "perimeter",
    }

    print(str(i) + ". For the following shape, determine the " + measure[measure_type])
    time.sleep(2)

    screen = turtle.getscreen()

    turtle.penup()
    turtle.goto(xlen / 2, ylen / 2)
    turtle.right(90)
    turtle.pendown()

    for n in range(4):
        if n % 2 == 0:
            turtle.forward(ylen)
            turtle.right(90)
        else:
            turtle.forward(xlen)
            turtle.right(90)

    # Write side lengths
    style = ("monospace", 10, "bold")
    text.showturtle()
    text.penup()
    text.goto(0, ((ylen / -2) - 20))
    text.pendown()
    text.write(str(int(xlen/25)), font=style, align="center")
    text.penup()
    text.goto((xlen / 2) + 20, -10)
    text.pendown()
    text.write(str(int(ylen/25)), font=style, align="center")
    text.hideturtle()

    question = ("What do you think the " + measure[measure_type] + " is?")
    guess = screen.numinput("Answer", question, 16, minval=1, maxval=144)
    turtle.reset()
    text.reset()
    turtle.color("magenta")
    text.color("aqua")

    if measure_type == 1:
        ans = (xlen / 25) * (ylen / 25)
    else:
        ans = (xlen / 25 * 2) + (ylen / 25 * 2)
    if guess == ans:
        print("Correct!!")
        mark += 1
    else:
        print("\033[1;31;40m")
        mark -= 1
        print("Incorrect, answer was:", str(ans) + ". Try again: ")
        questions(i, turtle, text)


def game():
    print("\033[1;34;40m")

    # Get Name
    name = functions.try_hard_check(input("What is your name? \n").title() or "Generic User")

    # Start question sequence
    turtle = Turtle()
    turtle.color("magenta")
    screen = turtle.getscreen()
    screen.bgcolor("black")

    text = Turtle()
    text.color("aqua")

    start_time = count()
    for i in range(12):
        questions(i+1, turtle, text)
    end_time = count()
    screen.bye()

    # Determine Score
    score = round(end_time - start_time, 2)

    # Determine Mark
    global mark
    functions.mark(score, mark)
    mark = 0

    # Change to ending music
    music.game_state = 2

    # Send to leaderboard
    if db.get_conf()["ONLINE"] is True and db.get_conf()["DECIMALS"] is False:
        lb(name, score)

    while True:
        if music.done:
            break

    if not db.get_conf()["MUSIC"]:
        time.sleep(5)

    print("\n" * 10)


def geometry():
    # Start Sequence
    functions.clear()
    print("\033[1;31;40m")
    fig = Figlet(font="larry3d")
    print(fig.renderText("Geometry Galore"))
    time.sleep(2)
    fig = Figlet(font="digital")
    print(fig.renderText("BY ROHAN SHIRKHEDKAR"))
    time.sleep(1)

    print("\033[1;35;40m")
    print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("| Welcome to Geometry Galore!!!                                                                         |")
    print("| Find the perimeter/area in randomly generated squares as fast as you can                              |")
    print("| You will be given a mark out of 12 as well as a grade at the end (This wont go on the leaderboard)    |")
    print("÷ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ×")
    time.sleep(1)
    print("\n")
    game()
