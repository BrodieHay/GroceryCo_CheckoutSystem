from GroceryCo_CheckoutSystem.products import insert_products


def test_answer():
    str = "apple 1 orange 2 watermelon 5"
    assert insert_products(str) == {'apple':{'key': "apple", 'price': 1},
                                'orange':{'key': "orange", 'price': 2},
                                'watermelon': {'key': "watermelon", 'price': 5}
                                }
