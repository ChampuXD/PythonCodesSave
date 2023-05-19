class school:
    def __init__(self,student,roll):
        self.student = student
        self.roll = roll
    def display(self):
        print(self.student,self.roll)

s1 = school("Shivanshu", 2201010012)
s1.display()
