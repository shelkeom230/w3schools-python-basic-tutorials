# access list items 
thislist=['apple','banana','kiwi','watermelon','papaya','akrod']
print(thislist[1])
print(thislist[-1])

# range of indexes 
print(thislist[0:1])

print(thislist[-1:])

print("apple" in thislist)
print("orange" not in thislist)

thislist[2]="mango"
print(thislist)

thislist[1:3]=['omkar','shelke']
print(thislist)

thislist.insert(1,"devesh")
print(thislist)

thislist.append("kshitij")
print(thislist)

states=['maharashtra','gujrat','punjab']
capitals=['mumbai','ahmadbad','amritsar']
states.extend(capitals)
print(states)

thislist=['apple','banana','kiwi']
thistuple=('kiwi','orange')
thislist.extend(thistuple)
print(thislist)


thislist.remove('apple')
print(thislist)

thislist.pop(1)
print(thislist)

del thislist[0]
print(thislist)

'''
del deletes entire list
clear() empties the list'''

# list comprehension 
fruits=['apple','banana','kiwi','cherry','mango']
newlist=[x for x in fruits if 'a' in x]; print(newlist)
newlist=[x for x in fruits if x !='apple']; print(newlist)
newlist=[x for x in fruits]; print(newlist)
newlist=[x for x in range(10)]; print(newlist,end=' ')
print()
newlist=[x for x in range(10) if x<5]; print(newlist)
newlist=['omkar','pramod','shelke']; uppercase=[x.upper() for x in newlist]; print(uppercase)
newlist=['hello' for x in newlist]; print(newlist)