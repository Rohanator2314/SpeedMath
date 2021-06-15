import os
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep

name = ""


def get_name():
    global name

    if not name:
        name = try_hard_check(input("What is your name? \n").title() or "Generic User")
    
    return name


def mark(score, mark):
    # Determine and give mark
    print("Your time is", str(score), "and your mark is", str(mark), "out of 12")
    grade = (mark / 12) * 100
    if grade > 89:
        print("You got an A")
        print("You did good")
    elif grade > 79:
        print("You got an B")
        print("Well done, hopefully you do better next time")
    elif grade > 69:
        print("You did well")
        print("Next time, try harder!")
    elif grade > 59:
        print("You just need to improve a little")
        print("Try not to throw questions")
    else:
        print("You didn't get many questions right")
        print("Next time, try for real to get questions right, remember to think them through")


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def try_hard_check(i):
    if i in ["Darcy", "Jack", "Will"]:
        i += " (Try Hard)"
    return i


class Loader:
    def __init__(self, desc="Loading...", end="Done!", timeout=0.1):
        """
        Takes in Arguments:
            desc (str, optional): The loader's description. Defaults to "Loading...".
            end (str, optional): Final print. Defaults to "Done!".
            timeout (float, optional): Sleep time between prints. Defaults to 0.1.
        """
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        # self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.steps = ['|', '/', '—', '\\'] # Need to escape backslash with backslash
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()
