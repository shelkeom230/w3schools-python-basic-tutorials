# while loops 
i=1
while i<10:
    print(i)
    i+=1
else: print("i am no longer less than 10")

# for loop 
fruits=['apple','banana','kiwi','ornage','banana','mango']
for x in fruits: print(x)
 
for x in 'banana': print(x)
print()
for x in fruits: 
    print(x)
    
    if x=='banana':
        break

for x in range(5): print(x)

for x in range(2,5): print(x)
print()

for x in range(1,10,2): print(x)
else: print("finally finised")

for x in range(6):
    if x==3: break
else: 
    print("finally finised")

cities=['mumbai','ahmadbad','jalandhar']
states=['maharashtra','gujrat','punjab']
for x in cities:
    for y in states:
        print(x,y)