from lib.password_checker import *
import pytest


# want to check that the length password is greater than 8, it should return True

def test_length_is_greater_than_8():
    password_checker = PasswordChecker()
    assert password_checker.check("23434343434") == True


# test to check it is equal to 8 first

def test_length_is_equal_to_8():
    password_checker = PasswordChecker()
    assert password_checker.check("12345678") == True

# test to check whether when it is incorrect passowrd, that there is an error message
    
def test_correct_output_error():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("invalid")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

# do i need this??
#test to check that there is length statement of password 
# def test_check_length_of_password():    
#     password_checker = PasswordChecker()
#     password = "blob"
#     assert len(password) == 4



