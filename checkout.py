#!/usr/bin/python

import sys
from collections import namedtuple

Products = {'banana': {'price': 4, 'key': 'banana'},
         'apple':  {'price': 2, 'key': 'apple'},
         'orange': {'price': 1.5, 'key': 'orange'},
         'pear':   {'price': 3 ,'key': 'pear'},
         'milk' : {'price': 10, 'key': 'milk'}
        }

#Create a shopping cart to hold the groceries
cart = []
#Put all of the groceries into the cart
fullList = sys.argv
fullList = fullList[1:]
for item in fullList:
    item = item.lower()
    cart.append(item)
#Get the grocery Bag ready for the scanned products
Bag = {}
#Start checking out the items in the cart
print("\nWelcome to the GroceryCo Checkout system!\n")

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
print("\nChecking out...\n")
sum=0
print('{:<10s}{:>4s}{:>10s}{:>12s}'.format("Amount","Item","Each","Subtotal"))
for item in Bag:
  print('  {:<8d}{:<10s}{:^5.2f}{:^15.2f}'.format(Bag[item]['amount'],Products[item]['key'],Products[item]['price'],Bag[item]['price']))
  sum+=Bag[item]['price']
print("\nThe total cost is: $",sum)
