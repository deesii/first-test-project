from lib.check_codeword import *

# if the codeword is correct
# returns "Correct! Come in."

def test_with_correct_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

# If the codeword is wrong 
# returns "WRONG!"
    
def test_with_incorrect_codeword():
    result = check_codeword("water")
    assert result == "WRONG!"

# If the codeword has the right first and last letter
#returns " close , but nope"
    
def test_with_close_codeword():
    result = check_codeword("house")
    assert result == "Close, but nope!"


# if the codeword has the right first letter and the wrong last one
# returns "Wrong!"
    
def test_with_mistakenly_close_codeword():
    result = check_codeword("hat")
    assert result == "WRONG!"

# if the codeword has the wrong first letter and the right last one
# returns "Wrong!"
    
def test_with_mistakenly_close_last_codeword():
    result = check_codeword("pie")
    assert result == "WRONG!"