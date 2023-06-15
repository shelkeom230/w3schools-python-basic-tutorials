# functions 
def myfunc(name):
    print("hi, ",name)
myfunc("omkar shelke")

def printName(fname,lname):
    print(fname+' '+lname)
printName('omkar','shelke')

def myfunc(*kids):
    print("the youngest child is: "+kids[2])
myfunc('omkar','devesh','kshitij','karan')

def youngestChild(name1,name2,name3):
    print("the youngest child is: "+name1)
youngestChild(name1='omkar shelke',name2='devesh patil',name3='kshitij hadke')

# arbitary keyword args 
def myfunc(**kwargs):
    print("his last name is: "+kwargs['lname'])
myfunc(fname='omkar',lname='shelke')

# default parameter value 
def myName(fname,lname='shelke'):
    print(fname+' '+lname)
myName('omkar','shelke')
myName('omkar')
myName('devesh')

def printFoods(foods):
    for x in foods: print(x)
printFoods(['apple','banana','mango'])

def product(x,y):
    return x*y
print(product(10,11))

# recursion 
def tri_recursion(n):
    if (n>0):
        result=n+tri_recursion(n-1)
        print(result)
    else:
        result=0
    return result
tri_recursion(6)
