import math
import sys
from products import insert_products
from promotions import insert_promotions

def get_employee_id(products_dict, promotions_dict):
    #Program expects ane employee to log in and enter new products and promotions (promotions are optional)
    id_valid = False
    promo_valid = False
    while not(id_valid):
        user_input = input("If you are an Employee and would like to update pricing and promotions, enter Employee ID (e.g. 1234):\n")
        #get the employees id and checks that it is valid
        if user_input == "1234":
            id_valid = True
            #set id flag to true and prompt employees to enter products
            products_dict = get_items()
            #check if there are any promotions that need to be entered
            user_input=input("Are there any promotions? (Y/N)\n")
            if user_input == "Y" or user_input == "y":
                promo_valid = True
                promotions_dict = get_promos()
            elif user_input == "N" or user_input == "n":
                promo_valid = True
            else:
                print("That was not a valid input, please try again")
        else:
            #employee id invalid, prompt again
            print("That was not a valid ID, please try again\n")
    return products_dict, promotions_dict

def get_items():
    #gets user input from the shop employee to populate the product dictionary in products.py
    return insert_products()


def get_promos():
    #gets user input from the shop employee to populate the promotions_dict dictionary in promotions.py
    return insert_promotions()

def get_grocery_list(bag, products_dict):
    #Gets the customers grocery list from the command line input
    user_input = input("Please enter your grocery list:\n")
    #Create a shopping cart to hold the groceries
    cart = list(map(str, user_input.split()))
    #Put all of the groceries into the cart
    i = 0
    for item in cart:
        lowered_item = item.lower()
        cart[i] = lowered_item
        i+=1
    #Start checking out the items in the cart

    for item in cart:
        if item in products_dict:
            #item exists in inventory
            if item in bag:
                #check if there are already same items in the cart
                bag[item]['amount']+=1
                bag[item]['price']+=products_dict[item]['price']
            else:
                #if this is the first time the bag is seeing this item we need to initialize it
                amount = 1
                price = products_dict[item]['price']
                bag[item] = {'amount': amount, 'price': price}
        else:
            #Tell customer about none existent items but continue to checkout
            print(item,"does not exist in inventory")
    return bag

def apply_promos(bag, products_dict, promotions_dict, promo_list):
    #check if a promotion exists for each item in bag and apply existing promos
    for item in bag:
        if item in promotions_dict:
            #promo exists for this item
            if bag[item]['amount'] >= promotions_dict[item]['amount']:
                #check if customer is buying enough items for promo to apply
                promo_amount = bag[item]['amount'] / promotions_dict[item]['amount']
                if promo_amount.is_integer():
                    #if all items apply for the promo
                    bag[item]['price'] = promotions_dict[item]['price'] * promo_amount
                else:
                    #if only an amount of the items apply for the discount
                    #   e.g. 2 for 1 but 3 items in bag
                    promo_amount_rounded = math.floor(promo_amount)
                    bag[item]['price'] = bag[item]['price'] - (promotions_dict[item]['amount'] * products_dict[item]['price'])
                    bag[item]['price'] = bag[item]['price'] + (promo_amount_rounded * promotions_dict[item]['price'])
                promo_list = promo_list + 'Promotion: {:s} applied to {:s}\n'.format(promotions_dict[item]['promo'],products_dict[item]['key'])
    return promo_list

def checkout(bag, products_dict, promotions_dict, promo_list):
    #Takes the Grocery list provided by customer and and displays all the items in a sorted list
    #   along with a list of the promotions applied and the total cost
    print("Checking out...\n")
    sum=0
    print('{:<10s}{:>4s}{:>10s}{:>12s}'.format("Amount","Item","Each","Subtotal"))
    for item in bag:
        #formatting for the list (can be adjusted easily depending width of recipt)
        print('  {:<8d}{:<10s}{:^5.2f}{:^15.2f}'.format(bag[item]['amount'],products_dict[item]['key'],products_dict[item]['price'],bag[item]['price']))
        sum+=bag[item]['price']
    print("\n",promo_list)
    print("The total cost is: ${:.2f}".format(sum))
    return

def main():
    bag = {}
    products_dict = {}
    promotions_dict = {}
    promo_list = ""
    print("\nWelcome to the GroceryCo Checkout system!\n")
    products_dict, promotions_dict = get_employee_id(products_dict, promotions_dict)
    bag = get_grocery_list(bag, products_dict)
    promo_list = apply_promos(bag, products_dict, promotions_dict, promo_list)
    checkout(bag, products_dict, promotions_dict, promo_list)

if __name__ == "__main__":
    main()
