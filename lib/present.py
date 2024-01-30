# File: lib/present.py

#not clear from the video as to the context of the problem, however:

# the contents will be renamed to "num_presents"
class Present:
    def __init__(self):
        self.num_presents= None

    def wrap(self, num_presents):
        if self.num_presents is not None:
            raise Exception("Contents have already been wrapped.")
        self.num_presents = num_presents

    def unwrap(self):
        if self.num_presents is None:
            raise Exception("No contents have been wrapped.")
        return self.num_presents
