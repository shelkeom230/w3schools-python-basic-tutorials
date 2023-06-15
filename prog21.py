# conditionals 
a=50
b=100
if a>b: print(a,' is greater than ',b)
else: print(a,' is less than ',b)

marks=int(input("enter your marks out of 1900: "))

if marks<0 or marks>1900: print('marks must be greater than 0 and less than 1900')
elif marks>1800: print("A")
elif marks>1750 and marks<=1800: print('B')
elif marks>1600 and marks<=1750: print('C')
else: print(marks)

if a>b: print('a is greater than b')

x=int(input())
y=int(input())
print(x) if x>y else print(b)
print(x) if x>y else print('=') if x==y else print(y)

# nested if 
x=int(input())
if x>10:
    print(x,' is greater than 10')
    if x>20: print(x, ' is also greater than 20')
    else: print(x,' is less than 20')
    