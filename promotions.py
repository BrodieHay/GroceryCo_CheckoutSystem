def insert_promotions(user_input):
    promotions_dict = {}
    valid = False
    input_valid = True
    while not valid:
        if not input_valid:
            user_input = input("Please enter any promotions in format 'Product Amount Promotion Price' (e.g. apple 2 BOGO50 1):\n")
        new_promotions = list(map(str, user_input.split()))
        item_names = new_promotions[::4]
        i = 0
        if (len(new_promotions)/4).is_integer():
            for items in item_names:
                key = str(new_promotions[i])
                promo = str(new_promotions[i+2])
                try:
                    amount = int(new_promotions[i+1])
                    price = float(new_promotions[i+3])
                    d = {items:{'key': key, 'amount': amount, 'promo': promo, 'price': price}}
                    promotions_dict.update(d)
                    i+=4
                    valid = True
                except:
                    print("Prices must be decimal numbers (e.g. 1.00) and amounts must be round numbers (e.g. 5), please try again")
                    valid = False
                    input_valid = False
        else:
            print("Some promotion fields are missing, please try again")
            input_valid = False
    return promotions_dict
