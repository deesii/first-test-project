
from lib.high_value import * 
import pytest

# do not think this is needed because the first function captures the type alraeady
# def test_invalid_type_values():
#     highest_value_instance = HighValue(4,5)
#     assert type(highest_value_instance.value_first) == int 
#     assert type(highest_value_instance.value_second) == int 

# testing that during instanciation, the instance variables for value_first and value_second are correctly set given the input values.

def test_correct_attributes_at_instanciation():
    highest_value_instance = HighValue(4,5)
    assert highest_value_instance.value_first == 4
    assert highest_value_instance.value_second == 5

# testing that the output is showing the correct value is greater than the other value, given the inputs

def test_when_one_value_greater_than_other_outputs_the_correct_value_as_higher():
    highest_value_instance = HighValue(4, 3)
    assert highest_value_instance.get_highest() == "First value is higher"

    highest_value_instance = HighValue(3, 4)
    assert highest_value_instance.get_highest() == "Second value is higher"


#testing for when the input is showing the when the input is the same as the output to be "values are equal"

def test_check_when_both_inputs_the_same():
    highest_value_instance = HighValue(3, 3)
    assert highest_value_instance.get_highest() == "Values are equal"

# testing for that the first value increases by the amount added

def test_add_first_value_ouputs_adds_to_first_value():
    highest_value_instance = HighValue(4, 3)
    highest_value_instance.add(2, "first")
    assert highest_value_instance.value_first == 6

# testing for that the second value increases by the amount added
    
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
    highest_values_instance = HighValue(4,5)
    assert highest_values_instance.add( 5, "bob") == None

    # with pytest.raises(ValueError, match = "Invalid selection"):
    #     highest_values_instance(4, "Invalid selection")





