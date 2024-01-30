from lib.present import *
import pytest

# check that you can wrap and then unwrap you will get the number that we can unwrap

def test_wrap_then_available_for_unwrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33


# want to check that you are not wrapping an already wrapped present

def test_check_that_you_have_not_wrapped_a_present_already_wrapped():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(5)
    error_message = str(e.value)
    assert error_message == "Contents have already been wrapped."

# checking for whether the error is raised for when you have unwrapped before you have wrapped
    
def test_check_unwrapping_with_no_wrapping_first():
    present = Present()

    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."


#if we try to wrap an already wrapped prsent, the first wrapped value is preserved
    
def test_check_that_you_preserve_the_number_of_the_first_num_presents_and_do_not_override():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(5)
    
    assert present.unwrap() == 44
