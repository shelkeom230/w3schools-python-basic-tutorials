# inheritence 
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    
    def printname(self):
        return self.fname+" "+self.lname

class student(Person):
    def __init__(self, fname, lname,age):
        super().__init__(fname, lname)
        self.age=age
    
    def display(self):
        print(self.fname,self.lname,self.age)

    def welcome(self):
        print("welocome "+self.fname+" "+self.lname+" to wipro. I think you are ",self.age," years old")

obj=student("omkar","shelke",18); obj.display()
obj.welcome()
