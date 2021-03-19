# GroceryCo_CheckoutSystem
Checkout system created for the grocery store known only as GroceryCo

#How to run
Start the program by typing *python3 checkout.py" into the terminal
  you will then be prompted to enter your employee ID, which is 1234
  after entering your employee ID you will be prompted to enter the products that are currently available (products are not saved on program exit in this version)
  ensure that you enter the products in the given format, as you may not proceed without doing so
  once all the new products are entered, you will be prompted to enter any promotions, if they exist
  once promotions are entered or you state that no promotions are currently available, the terminal is ready for the "customer" (also you)
  you will be prompted to insert your grocery list as a single line of unsorted single items, as if you were going through a self checkout at a store and scanning items yourself
  once the list is given, available promotions will be applied and your total will be calculated
  Your receipt is then displayed on the screen, listing amounts of each product, their individual price and a subtotal.
      Promotions are listed and your grand total is provided at the bottom of your receipt.
  end of program

#Assumptions
Employees have must enter products every time that the program runs, I would suggest implementing file i/o in the future, with the option for employees to add and remove products
Employees have total power over naming products and promotions, so spelling errors are possible and lead to failures when the customer is entering their list
    (the products will be seen as not in inventory)
A product can only have a single promotion at any time, adding a new promotion for an item will overwrite the last
The entire program only runs once so multiple customers cant check out in one session. This is similar to a self checkout in that every transaction is a different session
