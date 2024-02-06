# 5 feb 2024
# Python ASCII RPG Tutorial #1 
# playlist:
# https://www.youtube.com/watch?v=iMS75wmppew&list=PLIYv95CSVgLrlV8wkTAeOAHtw0It1NxT7&index=2

import os

run = True
menu = True
play = False
rules = False

HP = 50
ATK = 3

def clear():
    os.system("cls")
    
def draw():
    print("xX-----------------------------xX")
    
    

def save():
    list = [
        name,
        str(HP),
        str(ATK),
        
    ]
    f = open("load.txt", "w")
    
    for item in list:
        f.write(item + "\n")
    f.close()
    
while run:
    while menu:
        clear()
        draw()
        print("1, NEW GAME")
        print("2, LOAD GAME")
        print("3, RULES")
        print("4, QUIT GAME")
        draw()
        
        if rules:
            print("I'm the creator of this game and these are the rules")
            rules = False
            choice = ""        
            input("> ")
        else:
            choice = input("# ")
        
        if choice == "1":
            clear()
            name = input("# what's your name, hero? ")
            menu = False
            play = True
        elif choice == "2":
            f = open("load.txt", "r")
            load_list = f.readlines()
            name = load_list[0][:-1]
            HP = load_list[1][:-1]
            ATK = load_list[2][:-1]
            clear()
            print("Welcome back, " + name + "!")
            input("> ")
            menu = False
            play = True
            #print(name, HP, ATK)
        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()

    
    while play:
        #print(name)
        save() # autosaving
        clear()
        draw()
        print("0 - SAVE AND QUIT")
        draw()
        
        
        dest = input("# ")
        
        if dest == "@":
            play = False
            menu = True
            save() # manual saving