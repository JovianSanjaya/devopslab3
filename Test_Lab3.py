import Lab3

print("Test_Lab3")

def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_result = []
    result = Lab3.bubble_sort(input_arr, 3) # it's invalid because there's no sorting order 3

    assert (result == test_result)

def test_bubble_sort_morethanten():
    result = []
    input_array = [64, 34, 25, 12, 22, 11, 90 , 26 , 78 , 36 , 74 , 68 , 47]
    test_result = 1
    result = Lab3.bubble_sort(input_array, Lab3.SORT_ASCENDING)

    assert (result == test_result)

def test_bubble_sort_zero():
    result = []
    input_array = []
    test_result = 0
    result = Lab3.bubble_sort(input_array, Lab3.SORT_ASCENDING)

    assert (result == test_result)

def test_bubble_sort_non_interger():
    result = []
    input_array = ["sp", "is", "so","possible"]
    test_result = 2
    result = Lab3.bubble_sort(input_array, Lab3.SORT_ASCENDING)

    assert (result == test_result)