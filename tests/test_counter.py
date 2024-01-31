from lib.counter import *

# want to report that the output correct ouput when the count is initially counts zero

def test_counter_initially_reports_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

# want to report for when I am adding single number , could also check for individual class that assert self.count == 2
def test_counter_add_single_number():
    counter = Counter()
    counter.add(2)
    result = counter.report()
    assert result == f"Counted to 2 so far."

# report for adding multiple numbers to counters, that the sum is the final count
    
def test_counter_multiple_numbers():
    counter = Counter()
    counter.add(2)
    counter.add(3)
    result = counter.report()
    assert result == f"Counted to 5 so far."


# report for adding multiple numbers to counters, that the sum is the final count
    
def test_counter_triple_add():
    counter = Counter()
    counter.add(2)
    counter.add(3)
    counter.add(4)
    result = counter.report()
    assert result == f"Counted to 9 so far."

