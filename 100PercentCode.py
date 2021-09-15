#!/usr/bin/env python3
# -*- coding: utf-8 -*-



#Team Code Section
import pandas
foodsdf=pandas.read_csv("foods.csv")
entreeslist = list(foodsdf.Entrees)
sideslist = list(foodsdf.Sides)
drinkslist = list(foodsdf.Drinks)
def greet_user(greeting,sentinel,categoryq,readyq):
    canswer = ' '
    ranswer = sentinel
    print(greeting)
    while ranswer == sentinel:
        canswer = input(categoryq)
        ranswer = input(readyq)
    if canswer == "Entrees":
        entrees("Welcome to our Entrees section! Here are your choices:",entreeslist,"Which Entrees would you like or enter None? ")
    elif canswer == "Sides":
        sides("Welcome to our Sides section!  Here are your choices:",sideslist,"Which Sides would you like or enter None? ")
    elif canswer == "Drinks":
        drinks("Welcome to our Drinks section!  Here are your choices:",drinkslist,"Which Drinks would you like or enter None? ")
    else:
        print('Sorry, we do not carry that category.  See you next time!')


#Shabir Code Section
def entrees(greeting,selection,pickq):
    print(greeting)
    for item in selection:
        print(item)
    entreespick = input(pickq)
    if entreespick == "None":
        print("Goodbye")
    elif entreespick == "Hotdog":
        closing("Hotdog",5,"Enjoy your Hotdog!" )
    elif entreespick == "Hamburger":
        closing("Hamburger",5,"Enjoy your Haburger!" )
    else:
        closing("Corndog",5,"Enjoy your Corndog!" )
        
#Cynthia Code Section
def sides(greeting,selection,pickq):
    print(greeting)
    for item in selection:
        print(item)
    sidespick = input(pickq)
    if sidespick == "None":
        print("Goodbye")
    elif sidespick == "Fries":
        closing("Fries",5,"Enjoy your Fries!" )
    elif sidespick == "Pie":
        closing("Pie",5,"Enjoy your Pie!" )
    elif sidespick == "Cookie":
        closing("Cookie",5,"Enjoy your cookie!" )
    else:
        closing("Sides",150,"Enjoy your Sides!" )
#Eric Code section    
def drinks(greeting,selection,pickq):
    print(greeting)
    for item in selection:
        print(item)
    drinkspick = input(pickq)
    if drinkspick == "None":
        print("Goodbye")
    elif drinkspick == "Lemonade":
        closing("Lemonade",3,"Enjoy your Lemonade!" )
    elif drinkspick == "Water":
        closing("Water",2,"Enjoy your Water!" )
    elif drinkspick == "Soda":
        closing("Soda",5,"Enjoy your Soda!" )
    else:
        closing("Drinks",150,"Enjoy your Drinks!" )    

#Maria Code section
#Function to give user total price of purchase
def closing(pickeditem,price,goodbye):
    print("Your cost for the",pickeditem,"is $"+str(price))
    more = input("Would you like to pick another item (y/n)?")
    if more == "y":
        greet_user("Great!", "n", "What category would you like to browse (Entrees, Sides, Drinks)? ", "Ready to browse (y/n)? ")
    else:
        for l in goodbye:
            print(l)
    
    
        
greet_user("Welcome to our store", "n", "What category would you like to browse (Entrees, Sides, Drinks)? ", "Ready to browse (y/n)? ")
