# python sets 
# unordered, unchangable and unindexed, no duplicates

thisset={'apple','banana','kiwi'}
print(thisset)
newset=[x for x in thisset]; print(newset); print(len(thisset))

thisset=set(('apple','banana','orange')); print(thisset)

# set doesn't allows indexing 
# check if banana is present in the set 
print('banana' in thisset)

thisset.add('watermelon'); print(thisset)
animals=set(('tiger','lion','elephant'))
thisset.update(animals); print(thisset)

mylist=['omkar','pramod','shelke']
thisset.update(mylist); print(thisset)

# remove set items 
# remove()- raises an error if the item is not present 
# discard()- doesn't gives an error 
thisset.remove('omkar'); print(thisset)
thisset.discard('shelke'); print(thisset)

x=thisset.pop()
print(x); print(thisset)

'''
clear method empties the set
del method deltes the set entirely
'''
for x in thisset: print(x)


set1=set(('a','b','c')); set2={1,2,3}; set3=set1.union(set2); print(set3)

# update method also does the same as well 
set1.update(set2); print(set1)

# keep only the duplicates 
x={'apple','banana','cherry'}
y={'google','microsoft','apple'}
x.intersection_update(y)
print(x)

# intersection()- returns items identical in both the sets 
x.intersection(y); print(x)

# keep all but not the duplicates 
x.symmetric_difference_update(y); print(x)

# return only the elements that are not present in both the sets 
z=x.symmetric_difference(y); print(x)