import game.date.seaclet_answer as g
import random

def make_answer():
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    id = random.randint(0, 9)
    g.val1 = list.pop(id)

    id = random.randint(0, 8)
    g.val2 = list.pop(id)

    id = random.randint(0, 7)
    g.val3 = list.pop(id)

    id = random.randint(0, 6)
    g.val4 = list.pop(id)



def add_user_name(name):
    g.username = name