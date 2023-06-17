# iterators 
'''
an object that contains countable number of values
'''
# return an iterator from a tuple and print each value 
mytuple=('apple','banana','cherry')
myit=iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# strings are also iterable 
mystr="banana"
myit=iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

string="banana"
for x in string: print(x)

# create an iterator that returns numbers, starting from 1, and each sequence will increase by one (returning 1,2,3,4,5 etc)
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)