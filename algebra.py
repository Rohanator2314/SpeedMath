import db, re, math, time, random, music, functions
from decimal import *
from pyfiglet import Figlet
from time import perf_counter as count

mark = 0


def lb(name, score):
    # Add leaderboard Entry
    leaderboard_data = (name, score)
    db.add_db(leaderboard_data, 2)


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
        rand3 = rand(1, sml_range)
    elif operator == 3:
        rand1 = rand(1, sml_range)
        rand2 = rand(1, sml_range)
        rand3 = rand(1, sml_range)
    else:
        rand1 = rand(1, lrg_range)
        rand2 = rand(1, lrg_range)
        rand3 = rand(1, sml_range)

    rand1 = round(rand1, round_points)
    rand2 = round(rand2, round_points)
    str1 = str(rand1)
    str2 = str(rand2)
    str3 = str(rand3)
    real_str1 = str(rand1)
    real_str2 = str(rand2)

    str4 = "x"

    # Decide x position, c + or -
    xpos = random.randint(1, 4)
    ctype = random.randint(1, 2)

    if xpos == 1:
        str1 = "x"
    if xpos == 2:
        str2 = "x"
    if xpos == 3:
        str3 = "x"

    # Ask question and generate answer
    if operator == 4:
        ans = Decimal(real_str1) / Decimal(real_str2)
        question_string = (str1 + " ÷ " + str2)
    elif operator == 3:
        ans = Decimal(real_str1) * Decimal(real_str2)
        question_string = (str1 + " × " + str2)
    elif operator == 2:
        ans = Decimal(real_str1) - Decimal(real_str2)
        question_string = (str1 + " - " + str2)
    elif operator == 1:
        ans = Decimal(real_str1) + Decimal(real_str2)
        question_string = (str1 + " + " + str2)

    if ctype == 1:
        ans -= rand3
        question_string += (" - " + str3)
    else:
        ans += rand3
        question_string += (" + " + str3)

    if xpos != 4:
        str4 = str(ans)

    question_string += (" = " + str4)

    guess = Decimal(re.sub("[^0-9\-e\.]", "", input(str(i + 1) + ". Solve: " + question_string + "\n= ")) or 0)

    xans = {
        1: rand1,
        2: rand2,
        3: rand3,
        4: ans,
    }

    x = xans[xpos]

    if guess == x:
        print("Correct\n")
        mark += 1
    else:
        print("\033[1;31;40m")
        print("Incorrect, answer was:", str(x) + ". Try again: ")
        mark -= 1
        question(i)


def game():
    print("\033[1;33;40m")
    name = functions.try_hard_check(input("What is your name? \n").title() or "Generic User")

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
    print("\n"*10)


def algebra():
    # Start Sequence
    functions.clear()
    print("\033[1;35;40m")
    fig = Figlet(font="cricket")
    print(fig.renderText("Algebra X"))
    time.sleep(2)
    fig = Figlet(font="digital")
    print(fig.renderText("BY ROHAN SHIRKHEDKAR"))
    time.sleep(1)

    print("\033[1;36;40m")
    print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("| Welcome to the algebra problem game                                                                   |")
    print("| Find 'x' in 12 questions correctly as fast as you can to get to the top of the leaderboard!!          |")
    print("| You will be given a mark out of 12 as well as a grade at the end (This wont go on the leaderboard)    |")
    print("| If you want to restart type 'e' as your answer an type 'no' to exiting                                |")
    print("÷ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ×")
    time.sleep(1)
    print("\n")
    game()
