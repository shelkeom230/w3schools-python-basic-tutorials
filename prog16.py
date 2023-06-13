# sorting of lists 
thislist=['apple','banana','orange','kiwi','watermelon']
thislist.sort()
print(thislist)

numbers=[100,50,65,82,23]
numbers.sort(reverse=True); print(numbers)

# customize sort function 
def myfunc(n):
    return n-50
thislist=[100,50,65,82,23]
thislist.sort(key=myfunc)
print(thislist)

thislist.reverse(); print(thislist)

# copy lists 
thislist=['apple','banana','kiwi']
mylist=thislist.copy()
print(mylist)

mylist2=list(thislist); print(mylist2)

# join two lists 
list1=['a','b','c']; list2=[1,2,3]; print(list1+list2)

for x in list1: 
    list2.append(x)
print(list2)

for x in list1:
    list2.extend(x)
print(list2)