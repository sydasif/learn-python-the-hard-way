from sys import exit

def gold_room():
    pass


def silver_room():
    pass


def bear_room():
    pass



def chatalu_room():
    pass


def dead(why):
    print(why, "Good Bye!")
    exit(0)


def start():
    print("You enter in a dark room.")
    print("There are two door in dark room.")
    print("Where you want to go, left or right?")
    choice = input("> ")
    if choice == "left":
        bear_room()
    elif choice == "right":
        chatalu_room()
    else:
        dead("No more choice.")

start()
