# python string slicing 
b="hello world"
print(b[1:5])

# slicing from start 
print(b[:5])

print(b[2:])

print(b[:-1])

# modify strings 
a="hello , world"
print(a.upper())

print(a.lower())

print(a.strip())

print(a.replace('h','j'))

print(a.split(' , '))

# string conncatenation 
a="hello"
b=" omkar"
print(a+b)

# string formatting 
age=50
print("I am omkar and my age is {} years".format(18))


name=input()
age=int(input())
branch=input()

print("Hi, i am {} and i am {} years old and from {} branch".format(name,age,branch))

print("i like {1} and {0}".format("bread","butter"))