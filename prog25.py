# classes 
class myclass:
    x=5
obj=myclass()
print(obj.x)

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def __str__(self):
        return f"{self.name}({self.age})"
    
    def agedisplay(self):
        print("after 3 years my age will be: ", self.age+3)
obj=student('omkar shelke',18)
obj.agedisplay()