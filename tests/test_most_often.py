# In your pair, write tests for this class in a file tests/test_most_often.py. Make sure to run pytest to check whether your tests are passing.

# To help guide you, think about these questions in your pair:

# What functionality does each of the methods in the class have?
# What sorts of types in the list might be testable?
# If we were only ever dealing with integers (let's say), then what sorts of interesting list contents at instantiation and later on (after adding new) could be worth including in the tests?
# How many different outcomes are there that are testable, from get_most_often() and do you have tests for those?
# Do your tests cover at least all of the core functionality of the class, even if you aren't testing every type in the list or every combination of inputs?





from lib.most_often import *
#Need to make sure when init, is the list we input. e.g. empty list returns empty
def test_instantiate_empty_list():
    most_often = MostOften([])
    assert most_often.starting_list == []
#when add_new appending, actually appends
def test_append_new_item_check_list_adds_in():
    most_often = MostOften([])
    most_often.add_new("bobby")
    assert most_often.starting_list == ["bobby"]
#test for when there is a clear winner
def test_check_for_winner():
    most_often = MostOften(["bobby","bobby",1,1,1,2,2,3,"dobby"])
    assert most_often.get_most_often() == 1
#Test when there are equal number of winners/variables. output = no clear winner
def test_check_for_no_clear_winner():
    most_often = MostOften(["bobby","bobby",1,2,3,"dobby","dobby"])
    assert most_often.get_most_often() == "no clear winner"
#Inputting a mix list, outputs the set by count
    
#Case for instantiating None 
    
def test_no_starting_list_inputted():
    most_often = MostOften(None)
    assert most_often.starting_list == None