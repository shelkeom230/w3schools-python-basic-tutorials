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

