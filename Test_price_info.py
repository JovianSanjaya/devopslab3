import price_info

def test_total_cost_shopping():
    result = price_info.total_cost_shopping()
    test_result = 46.75
    assert (result == test_result)

def test_cost_of_fruit():
    fruit = 'orange'
    quantity = 10
    result = price_info.cost_of_fruits(fruit,quantity)
    test_result = 14
    assert (result == test_result)

