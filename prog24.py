# python lambda functions 
x=lambda x:x+10
print(x(5))

add=lambda x,y: x+y; print(add(10,11))

product=lambda x:x*x; print(product(10))

def myfunc(n):
    product=lambda x:x*n
    return product
mydoubler=myfunc(10)
print(mydoubler(5))