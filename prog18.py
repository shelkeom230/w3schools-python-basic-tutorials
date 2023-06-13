# python sets 
# unordred, unchangable and unindexed 

thisset={'apple','banana','kiwi'}; print(thisset)

for x in thisset: print(x)
print(len(thisset))

thisset=set(('apple','watermelon','orange')); print(thisset)
print('watermelon' in thisset)

thisset.add('orange'); print(thisset)

tropical={'pineapple','mango','papaya'}
mylist=['kiwi','ornage']
thisset.update(mylist); print(thisset)

mylist.discard('pineapple'); print(mylist)