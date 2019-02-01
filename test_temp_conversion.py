from temp_conversion import convert_c_to_f
from temp_conversion import fever_detection


def test_convert_c_to_f():
    answer = convert_c_to_f(-40.0)
    expected = -40.0
    assert answer == expected

def test_2():
    answer = convert_c_to_f(20)
    expected = 68
    assert expected == answer

def test_fever_detection():
    temp_list = [93.0, 98.0, 100.0, 105.0, 101.0]
    max_temp, is_fever = fever_detection(temp_list)
    expectedMax = 105.0
    is_Fever = True
    assert max_temp == expectedMax
