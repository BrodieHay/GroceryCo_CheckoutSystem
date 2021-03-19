import sys

from groceryco_checkout_system.products import insert_products


def test_answer():
    user_input = "apple 1 orange 2 watermelon 5"
    assert insert_products(user_input) == {'apple':{'key': "apple", 'price': 1},
                                'orange':{'key': "orange", 'price': 2},
                                'watermelon': {'key': "watermelon", 'price': 5}
                                }
