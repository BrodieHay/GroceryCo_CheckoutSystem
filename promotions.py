#!/usr/bin/env python

Promotions = {}

def insertPromotions(userInput):
    newPromotions = list(map(str, userInput.split()))
    itemNames = newPromotions[::4]
    i = 0
    for items in itemNames:
        key = str(newPromotions[i])
        amount = float(newPromotions[i+1])
        promo = str(newPromotions[i+2])
        price = float(newPromotions[i+3])
        d = {items:{'key': key, 'amount': amount, 'promo': promo, 'price': price}}
        Promotions.update(d)
        i+=4
    return Promotions

def test_answer():
    str = "apple 2 BOGO50 1.5 orange 6 6for10 10 watermelon 2 BOGOFree 5"
    assert insertPromotions(str) == {'apple':{'key': 'apple', 'amount': 2, 'promo': 'BOGO50', 'price': 1.5},
                                'orange':{'key': 'orange', 'amount': 6, 'promo': '6for10', 'price': 10},
                                'watermelon': {'key': 'watermelon', 'amount': 2, 'promo': 'BOGOFree', 'price': 5}
                                }
