class Student:
    
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        
    def on_honour_roll(self):
        if self.gpa >= 3.5:
            honour_roll = print(self.name + " is on the honour roll")
           
        else:
            honour_roll = print(self.name + " is not on the honour roll")
           
        return honour_roll
