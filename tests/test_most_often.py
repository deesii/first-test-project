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