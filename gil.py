import random

def ex():
    r = random.randint(0,2)
    def morning():
        print("Good morning")

    def day():
        print("Good day")

    def night():
        print("Good evening")

    if r == 0:
        return morning
    if r == 1:
        return day
    if r == 2:
        return night

