import devopslab2.bmi as bmi

def test_bmi_normal_weight():
    weight_input = 57
    height_input = 1.73
    expected_result = 0
    result = bmi.calculate_bmi(height_input,weight_input)
    assert ( result == expected_result)

def test_bmi_over_weight():
    weight_input = 77
    height_input = 1.53
    expected_result = 1
    result = bmi.calculate_bmi(height_input,weight_input)
    assert ( result == expected_result)

def test_bmi_under_weight():
    weight_input = 40
    height_input = 1.83
    expected_result = -1
    result = bmi.calculate_bmi(height_input,weight_input)
    assert ( result == expected_result)
