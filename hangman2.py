import random
import sys
word = ["orange","lemon","paris","hi","bear","bye","berlin","southpaw","bing"]
chosen=random.choice(word) 
chosen_l=len(chosen)
def intro():
    name = input("enter your name: ")
    print("Welcome",name," to HANGMAN\n")
    return name


def guessing(chosen_l,name):
    the_guess = ""
    trials = 0 
    while trials < 11:
        for i in chosen:
            if i in the_guess:
                sys.stdout.write(i)
            else:
                sys.stdout.write("_ ")
        if len(the_guess)==chosen_l:
            print("\nYOU HAVE WON ",name,"!")
            break
        your_guess = input(str.lower("\nenter a letter\n"))
        if len(your_guess)==1:       
            if your_guess in chosen:
                the_guess+=your_guess
                print("that is right")
            if your_guess not in chosen:
                trials += 1
                print("wrong think again")
            if trials == 11:
                print("you have lost ",name)
        elif len(your_guess)!=1:
            print("Please input one letter")        

name=intro()     
guessing(chosen_l,name)