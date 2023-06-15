# dictionaries 
thisdict={
    'brand':'ford',
    'model':'mustang',
    'year':1964
}

# key:value pairs, ordred, changeable and do not allow duplicates 
for x in thisdict: print(thisdict[x])
print(thisdict['brand'])
print(len(thisdict))
print(type(thisdict))

# dict constructor 
thisdict=dict(name='omkar shelke',age=18,branch='cse',year=2020)
print(thisdict)

# get the value of age 
x=thisdict.get('age')
print(x)

x=thisdict.keys(); print(x)

x=thisdict.values(); print(x)

x=thisdict.items(); print(x)

if 'model' in thisdict: print('yes')
else: print("no")

# change dictionary 
thisdict['model']='maruti suzuki'
print(thisdict)

thisdict.update({'age':23})
print(thisdict)

thisdict.pop('name')
print(thisdict)

thisdict.popitem(); print(thisdict)

'''
del thisdict['model']
thisdict.clear()
'''

for x in thisdict: print(thisdict[x])

mydict=thisdict.copy()
print(mydict)

mydict2=dict(thisdict)
print(mydict2)