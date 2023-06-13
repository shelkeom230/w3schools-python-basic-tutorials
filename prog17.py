# tuples 
# ordered and unchangable allow duplicates

thistuple=("apple",'banana','''orange''')
print(thistuple)

for x in thistuple: print(x)

print(len(thistuple))

# tuple with one item 
thistuple=('apple',); print(type(thistuple))
thistuple=tuple(('apple','banana','kiwi')); print(thistuple)

# access items 
print(thistuple[1])
print(thistuple[-1])
print(thistuple[1:3])

if 'apple' in thistuple: print("yes, \'apple\' is present in this tuple")

# change tuple values 
y=list(thistuple)
y[0]='orange'
y.append('watermelon')
thistuple=tuple(y)
print(thistuple)

# add tuple to a tuple
y=('apple',) 
thistuple+=y
print(thistuple)


# unpacking a tuple 
tup1=(1,2,3); a,b,c=tup1; print(a,b,c)

# loop through a tuple 
for x in thistuple: print(x)
print()

for x in range(len(thistuple)): print(thistuple[x])

i=0
while i<len(thistuple): print(thistuple[i]); i+=1

# join tuples 
tup1=(1,2,3); tup2=(4,5,6); print(tup1+tup2)

print(tup1*2)