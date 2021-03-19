#!/usr/bin/env python

import math
import sys
from products import Products
from products import insertProducts
from promotions import Promotions
from promotions import insertPromotions

#Get the grocery Bag ready for the scanned products
Bag = {}

def getEmployeeId():
    #Program expects ane employee to log in and enter new Products and Promotions (Promotions are optional)
    idValid = False
    promoValid = False
    while not(idValid):
        userInput = input("If you are an Employee and would like to update pricing and promotions, enter Employee ID (e.g. 1234):\n")
        #get the employees id and checks that it is valid
        if userInput == "1234":
            idValid = True
            #set id flag to true and prompt employees to enter products
            getItems()
            while not(promoValid):
                #check if there are any promotions that need to be entered
                userInput=input("Are there any promotions? (Y/N)")
                if userInput == "Y" or userInput == "y":
                    promoValid = True
                    getPromos()
                elif userInput == "N" or userInput == "n":
                    promoValid = True
                else:
                    print("That was not a valid input, please try again")
        else:
            #employee id invalid, prompt again
            print("That was not a valid ID, please try again\n")
    return

def getItems():
    #gets user input from the shop employee to populate the product dictionary in products.py
    userInput = input("Please enter the pricing rules in format 'Product Price' (e.g. apple 0.75 orange 1):\n")
    insertProducts(userInput)
    return

def getPromos():
    #gets user input from the shop employee to populate the promotions dictionary in promotions.py
    userInput = input("Please enter any promotions in format 'Product Amount Promotion Price' (e.g. apple 2 BOGO50 1):\n")
    insertPromotions(userInput)
    return

def getGroceryList():
    #Gets the customers grocery list from the command line input
    userInput = input("Please enter your grocery list:\n")
    #Create a shopping cart to hold the groceries
    cart = list(map(str, userInput.split()))
    #Put all of the groceries into the cart
    i = 0
    for item in cart:
        loweredItem = item.lower()
        cart[i] = loweredItem
        i+=1
    #Start checking out the items in the cart

    for item in cart:
        if item in Products:
            #item exists in inventory
            if item in Bag:
                #check if there are already same items in the cart
                Bag[item]['amount']+=1
                Bag[item]['price']+=Products[item]['price']
            else:
                #if this is the first time the Bag is seeing this item we need to initialize it
                amount = 1
                price = Products[item]['price']
                Bag[item] = {'amount': amount, 'price': price}
        else:
            #Throw error for none existent items but continue to checkout
            print(item,"does not exist in inventory")
    return

def applyPromos():
    #check if a promotion exists for each item in Bag and apply existing promos
    for item in Bag:
        promoList = ""
        if item in Promotions:
            #promo exists for this item
            if Bag[item]['amount'] >= Promotions[item]['amount']:
                #check if customer is buying enough items for promo to apply
                x = Bag[item]['amount'] / Promotions[item]['amount']
                if x.is_integer():
                    #if all items apply for the promo
                    Bag[item]['price'] = Promotions[item]['price'] * x
                else:
                    #if only an amount of the items apply for the discount
                    #   e.g. 2 for 1 but 3 items in Bag
                    xRounded = math.floor(x)
                    Bag[item]['price'] = Bag[item]['price'] - (x * Products[item]['price'])
                    Bag[item]['price'] = Bag[item]['price'] + (x * Promotions[item]['price'])
                promoList = 'Promotion: {:s} applied to {:s}\n'.format(Promotions[item]['promo'],Products[item]['key'])
    return promoList

def checkout(promoList):
    #Takes the Grocery list provided by customer and and displays all the items in a sorted list
    #   along with a list of the promotions applied and the total cost
    print("Checking out...\n")
    sum=0
    print('{:<10s}{:>4s}{:>10s}{:>12s}'.format("Amount","Item","Each","Subtotal"))
    for item in Bag:
        #formatting for the list (can be adjusted easily depending width of recipt)
        print('  {:<8d}{:<10s}{:^5.2f}{:^15.2f}\n'.format(Bag[item]['amount'],Products[item]['key'],Products[item]['price'],Bag[item]['price']))
        sum+=Bag[item]['price']
    print(promoList)
    print("The total cost is: ${:.2f}".format(sum))
    return

def main():
    print("\nWelcome to the GroceryCo Checkout system!\n")
    getEmployeeId()
    getGroceryList()
    promoList = applyPromos()
    checkout(promoList)

main()
