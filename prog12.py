# boolean values 
print(10>9); print(10<9); print(10==10); print(10>=10); print(10<=5)

a=10
b=20

if a<b: print(a," is less than ",b)
else: print(a," is greater than ",b)

print(bool("omkar shelke"))
print(bool(10))

x="hello"
y=50
print(bool(x),bool(y))

'''
any string is true, except empty
any number is true, except 0
any list, tuple, set and dict are true, except empty ones'''

print(False)
print(bool([]))
print(bool(""))
print(bool(()))
print(bool({}))

class myclass:
    def __len__(self):
        return 0
obj=myclass()
print(bool(obj)) #returns false

# functions can return boolean 
def myfunc():
    return True

if myfunc(): print("yes")
else: print("no")
# print(myfunc())

x=200
print(isinstance(x,int))