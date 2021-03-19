#!/usr/bin/env python

Products = {}

def insertProducts(userInput):
    newProducts = list(map(str, userInput.split()))
    itemNames = newProducts[::2]
    i = 0
    for items in itemNames:
        key = str(newProducts[i])
        price = float(newProducts[i+1])
        d = {items:{'key': key, 'price': price}}
        Products.update(d)
        i+=2
    return Products

def test_answer():
    str = "apple 1 orange 2 watermelon 5"
    assert insertProducts(str) == {'apple':{'key': "apple", 'price': 1},
                                'orange':{'key': "orange", 'price': 2},
                                'watermelon': {'key': "watermelon", 'price': 5}
                                }
