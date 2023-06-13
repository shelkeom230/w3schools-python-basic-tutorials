# global variables 
var="awesome"

def foo():
    print("python is "+var)

foo()


def myfunc():
    x="fantastic"
    print("python is "+x)

myfunc()
print("python is "+var)


def myfun():
    global x
    x="fantastic"
myfun()
print("value of x: "+x)