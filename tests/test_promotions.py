from GroceryCo_CheckoutSystem.promotions import promotions_dict, insert_promotions

def test_answer():
    str = "apple 2 BOGO50 1.5 orange 6 6for10 10 watermelon 2 BOGOFree 5"
    assert insert_promotions(str) == {'apple':{'key': 'apple', 'amount': 2, 'promo': 'BOGO50', 'price': 1.5},
                                'orange':{'key': 'orange', 'amount': 6, 'promo': '6for10', 'price': 10},
                                'watermelon': {'key': 'watermelon', 'amount': 2, 'promo': 'BOGOFree', 'price': 5}
                                }
