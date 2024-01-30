# File: tests/test_reminde_2.py

from lib.reminder_2 import *

# in this test case, there is no task added which it should be for def remind_me_to(self,task)

# def test_reminder():
#     reminder = Reminder("Kay")
#     result = reminder.remind()


#     assert result == "No reminder set!"

# it should pass with the logic, but when you want to test for errors, the test doesnt work like that.

#adjusting the test case

# File: tests/test_reminder.py


import pytest # <-- New code


def test_reminds_the_user_to_do_a_task():
    reminder = Reminder_2("Donna")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind()
    assert result == "Walk the dog, Donna!"


def test_reminder():
    reminder = Reminder_2("Kay")
    with pytest.raises(Exception) as e: 
    # <-- We use with pytest.raises(Exception) as e: to set up a section 
    #of the code where we expect an error to happen and then be caught by pytest.
        reminder.remind()
    error_message = str(e.value) # to get the error message that was generated
    assert error_message == "No reminder set!" #assert that it is the correct one. 
    # if is not equal to that , as it should be in the above, because no task is given, then the test fails. 

# All you need to remember for now is that when you are testing for errors, you can use the above syntax.
    # i think this means if you are testing for errors in the source code! 