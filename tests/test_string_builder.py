from lib.string_builder import *

#testing for adding the output that it is empty string to start

def test_string_empty_output_empty():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

# testing for adding a string that only ouputs that string you have added
    
def test_string_adding_one_string_that_outputs_that_string():
    string_builder = StringBuilder()
    string_builder.add("bla")
    assert string_builder.output() == "bla"

# testing for adding multiple strings and outputs also.
    
def test_string_adding_one_string_that_outputs_multiple_strings():
    string_builder = StringBuilder()
    string_builder.add("bla")
    string_builder.add("bla")
    result = string_builder.output() # creating a new variable doesnt change the assertion
    assert result == "blabla"

# testing for length 
    
# testing the output with one string added
    
def test_size_string_with_output_that_one_string():
    string_builder = StringBuilder()
    string_builder.add("bla")
    result = string_builder.size()
    assert result == 3

#testing the output with more than one string added.
    
def test_size_string_with_output_with_multiple_strings():
    string_builder = StringBuilder()
    string_builder.add("bla")
    string_builder.add("bla")
    result = string_builder.size()
    assert result == 6


