# File: lib/reminder_2.py
# this is where I want my clas to throw an error..

class Reminder_2:
    def __init__(self, name):
        self.name = name
        self.task = None

    def remind_me_to(self, task):
        self.task = task

    def remind(self):
        # Look here! We want to fail if there is no reminder yet.
        if self.task is None:
            raise Exception("No reminder set!")
        return f"{self.task}, {self.name}!"

# If the condition self.task is None evaluates to True (meaning there is no 
#reminder set), the code raises an exception. The exception raised is a generic Exception 
#with the message "No reminder set!"
    
# when there is an error raised by exceptions, it cuts the program without returning the next line,
# lines even if the inputs are correct! 