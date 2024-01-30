from lib.report_length import *

#test for when there is a string

def test_report_with_string():
    result = report_length("happy")
    assert result == "This string was 5 characters long."


#test for when there is no string
def test_report_with_0_length_string():
    result = report_length("")
    assert result == "This string was 0 characters long."