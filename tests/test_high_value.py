
from lib.high_value import * 
import pytest


# def test_invalid_type_values():
#     highest_value_instance = HighValue(4,5)
#     assert type(highest_value_instance.value_first) == int 
#     assert type(highest_value_instance.value_second) == int 

def test_correct_attributes():
    highest_value_instance = HighValue(4,5)
    assert highest_value_instance.value_first == 4
    assert highest_value_instance.value_second == 5


def test_get_highest():
    highest_value_instance = HighValue(4, 3)
    assert highest_value_instance.get_highest() == "First value is higher"

    highest_value_instance = HighValue(3, 4)
    assert highest_value_instance.get_highest() == "Second value is higher"

    highest_value_instance = HighValue(3, 3)
    assert highest_value_instance.get_highest() == "Values are equal"


def test_add_first_value():
    highest_value_instance = HighValue(4, 3)
    highest_value_instance.add(2, "first")
    assert highest_value_instance.value_first == 6

def test_add_second_value():
    highest_values_instance = HighValue(4,3)
    highest_values_instance.add(2, "second")
    assert highest_values_instance.value_second == 5

# def test_invalid_type_values():

#     highest_values_instance = HighValue(4,3)
#     with pytest.raises(Exception) as e:
#         highest_values_instance.get_highest()
#     error_message = str(e.value)
#     assert error_message == ""
    
def test_add_invalid_selection():
    highest_values_instance = HighValue()
    with pytest.raises(ValueError, match = "Invalid selection"):
        highest_values_instance(4, "Invalid selection")





