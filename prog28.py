# polymorphism 
x="hello world"
y=[1,2,3]
z=('a','b','c')
w={'omkar','pramod','shelke'}
colleges={
    'name':'bits pilani',
    'city':'ragasthan',
    'ranking':10
}

print(len(x))
print(len(y))
print(len(z))
print(len(w))

print()

# class polymorphism 
class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def move(self):
        print("driving the car")

class boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def move(self):
        print("Sail ")

class plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def move(self):
        print("fly ")

carobj=car("ford","mustang")
boatobj=boat("ibiza",'touring 20')
planeobj=plane("indigo",'747')
for x in (carobj,boatobj,planeobj):
    x.move()
