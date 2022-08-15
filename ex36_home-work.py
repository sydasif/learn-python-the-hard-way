from sys import exit

def gold_room():
    print("You are in gold room.")
    print("Gold room is full of gold.")
    print("How much do you take?")
    choice = int(input("> "))
    if choice == 1:
        print("Good, take it.")
    elif choice == 2:
        print("You win, take it.")
    else:
        if choice < 50:
            print("Take it.")
        else:
            dead("You Greedy Man.")    


def silver_room():
    print("chatalu is dead, and you are in silver room.")
    print("This room is full of silver.")
    print("Take it as you want. Bye!")
    exit(0)


def bear_room():
    print("You are in a bear room.")
    print("There is a huge bear in room.")
    print("Give it 'honey' or 'slap' the bear.")
    choice = input("> ")
    if choice == "honey":
        print("You saved your life.")
        gold_room()
    else:
        dead("You are dead man.")




def chatalu_room():
    print("You are in chatalu room.")
    print("A huge monster.")
    print("What to do now. Go 'back' or 'fight'.")
    
    while True:    
        choice = input("> ")
        if choice == 'back':
            dead("You suck!")
        elif choice == 'fight':
            silver_room()
        else:
            print("No way fight or go back.")


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
