import db, random, time, music, functions
from pyfiglet import Figlet


def lb(name, score):
    # Add leaderboard Entry
    leaderboard_data = (name, score)
    db.add_db(leaderboard_data, 4)


def game():
    # Get User Data
    print("\033[1;36;40m")
    name = functions.try_hard_check(input("What is your name? \n").title() or "Generic User")
    print("\033[1;31;40m")
    rang = int(input("What range of numbers do you want there to be? Between 1 and: \n"))
    tries = int(input("Ive made a random number, how many tries do you think it will take you to figure out the number? \n"))
    randNum = random.randint(1, rang)

    # Start Guessing
    print("\033[1;35;40m")
    guess = int(input("What do you think the random number is " + name + "?\n\n"))
    for i in range(tries):
        if guess == randNum:

            music.game_state = 2

            print("You got it " + name + "! The random number was " + str(randNum) + ". You had " + str(tries - (i + 1)) + " moves left")
            moves = i + 1
            score = rang / moves
            print("Your score was: " + str(score) + "\n")

            if db.get_conf()["ONLINE"]:
                lb(name, score)

            while True:
                if music.done:
                    break

            break
        elif i != tries - 1:
            if guess > randNum:
                guess = int(input("Too high! Guess again. You have " + str(tries - (i + 1)) + " moves left\n\n"))
            else:
                guess = int(input("Too low! Guess again. You have " + str(tries - (i + 1)) + " moves left\n\n"))
        else:
            print("You LOSE!!!! Mwahahahahaa! The random number was " + str(randNum))
            while True:
                if music.done:
                    break


def numguess():
    # Start Sequence
    functions.clear()
    print("\033[1;32;40m")
    fig = Figlet(font="chunky")
    print(fig.renderText("Guess the Number!!"))
    time.sleep(2)
    fig = Figlet(font="digital")
    print(fig.renderText("BY ROHAN SHIRKHEDKAR"))
    time.sleep(1)

    print("\033[1;33;40m")
    print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("| Welcome to the number guessing game                             |")
    print("| Guess the right number as fast as you can!!                     |")
    print("| Your score will be calculated as the range of numbers by the    |")
    print("| amount of tries it took you to get the answer                   |")
    print("÷ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ×")
    time.sleep(1)
    print("\n")
    game()
