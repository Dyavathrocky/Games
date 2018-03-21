#!/usr/bin/env python

import random

number = random.randint(1, 100)
tries =1

uname = input("hello , what is your name ")

print("Hello" , uname + ".",)

question = input ("would you like to play game ? [Y/N]")

if question =="n":
    print("ohhhh...okay")

if question == "y":
    print("i am thinking of a number between 1 & 10 ")
    guess = int(input("have a guuess dude : "))
    if guess > number :
        print("guess lower dude ")
    if guess < number :
        print ("guess high dude ....")
    while guess != number :
        tries += 1
        guess = int(input("try again : "))
        if guess > number:
            print ("guess lower ")
        elif guess < number:
            print("guess higher ")
        elif guess == number:
            print ("Cool dude you won the game , the number was " , number ,"and it only " , tries , "tries")
            
