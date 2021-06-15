import db, re, math, time, random, music, functions
from decimal import *
from pyfiglet import Figlet
from time import perf_counter as count

mark = 0


def lb(name, score):
    # Add leaderboard Entry
    leaderboard_data = (name, score)
    db.add_db(leaderboard_data, 1)


def question(i):
    # Change Colour
    print("\033[1;32;40m")

    # Get difficulty
    conf = db.get_conf()
    rand = random.randint
    round_points = 0
    dif = conf["DIFFICULTY"]

    global mark

    # Activate division operator on level 3 and above
    if conf["DIFFICULTY"] > 2:
        op_rang = 4
    else:
        op_rang = 3

    # Activate decimal points on level 4 and above
    if conf["DIFFICULTY"] > 3 and conf["DECIMALS"] is True:
        rand = random.uniform
        dif = math.ceil(conf["DIFFICULTY"] / 2)
        round_points = conf["DIFFICULTY"] - 3

    # Range variables
    lrg_range = dif * 50
    sml_range = dif * 6

    # Choose operator and random numbers
    operator = random.randint(1, op_rang)
    if operator == 4:
        while True:
            rand1 = round(rand(1, lrg_range), round_points)
            rand2 = round(rand(1, sml_range), round_points)
            result = rand1/rand2
            if result.is_integer():
                break
    elif operator == 3:
        rand1 = rand(1, sml_range)
        rand2 = rand(1, sml_range)
    else:
        rand1 = rand(1, lrg_range)
        rand2 = rand(1, lrg_range)

    rand1 = round(rand1, round_points)
    rand2 = round(rand2, round_points)
    rand1_str = str(rand1)
    rand2_str = str(rand2)

    # Ask question and generate answer
    if operator == 4:
        ans = Decimal(rand1_str) / Decimal(rand2_str)
        guess = Decimal(re.sub("[^0-9\-e\.]", "", input(str(i + 1) + ". What is " + rand1_str + " divided by " + rand2_str + "?\n= ")) or 0)
    elif operator == 3:
        ans = Decimal(rand1_str) * Decimal(rand2_str)
        guess = Decimal(re.sub("[^0-9\-e\.]", "", input(str(i + 1) + ". What is " + rand1_str + " times " + rand2_str + "?\n= ")) or 0)
    elif operator == 2:
        ans = Decimal(rand1_str) - Decimal(rand2_str)
        guess = Decimal(re.sub("[^0-9\-e\.]", "", input(str(i + 1) + ". What is " + rand1_str + " minus " + rand2_str + "?\n= ")) or 0)
    elif operator == 1:
        ans = Decimal(rand1_str) + Decimal(rand2_str)
        guess = Decimal(re.sub("[^0-9\-e\.]", "", input(str(i + 1) + ". What is " + rand1_str + " plus " + rand2_str + "?\n= ")) or 0)

    if guess == ans:
        print("Correct\n")
        mark += 1
    else:
        print("\033[1;31;40m")
        print("Incorrect, answer was:", str(ans) + ". Try again: ")
        mark -= 1
        question(i)


def game():
    print("\033[1;33;40m")
    name = functions.get_name()

    global mark

    print("\nStarting game... \n")

    for i in range(5):
        print(str(5-i) + "."*(5-i))
        time.sleep(1)

    # Ask Questions
    start_time = count()
    for i in range(12):
        question(i)
    end_time = count()

    # Change Colour
    print("\033[1;31;40m")

    # Determine Score
    score = round(end_time - start_time, 2)

    # Determine and give mark
    functions.mark(score, mark)

    # Change to ending music
    music.game_state = 2

    print("Showing you your leaderboard status now...")

    mark = 0

    # Send to leaderboard
    if db.get_conf()["ONLINE"] is True and db.get_conf()["DECIMALS"] is False:
        lb(name, score)

    while True:
        if music.done:
            break

    if not db.get_conf()["MUSIC"]:
        time.sleep(5)

    print("\n"*10)


def speedmath():
    # Start Sequence
    functions.clear()
    print("\033[1;36;40m")
    fig = Figlet(font="speed")
    print(fig.renderText("Speed Math"))
    time.sleep(2)
    fig = Figlet(font="digital")
    print(fig.renderText("BY ROHAN SHIRKHEDKAR"))
    time.sleep(1)

    print("\033[1;35;40m")
    print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("| Welcome to the math problem game                                                                      |")
    print("| Solve 12 questions correctly as fast as you can to get to the top of the leaderboard!!                |")
    print("| You will be given a mark out of 12 as well as a grade at the end (This wont go on the leaderboard)    |")
    print("| If you want to restart type 'e' as your answer an type 'no' to exiting                                |")
    print("÷ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ×")
    time.sleep(1)
    print("\n")
    game()
