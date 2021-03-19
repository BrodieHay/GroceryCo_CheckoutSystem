def insert_products():
    products_dict = {}
    valid = False
    while not valid:
        user_input = input("Please enter the pricing rules in format 'Product Price' (e.g. apple 0.75 orange 1):\n")
        new_products = list(map(str, user_input.split()))
        item_names = new_products[::2]
        i = 0
        for items in item_names:
            if (len(new_products)/2).is_integer():
                key = str(new_products[i])
                try:
                    price = float(new_products[i+1])
                    valid = True
                    d = {items:{'key': key, 'price': price}}
                    products_dict.update(d)
                    i+=2
                except:
                    print("Prices must be numbers (e.g. 5 or 1.00), please try again")
                    valid = False
            else:
                print("Some product fields are missing, please try again")
    return products_dict
