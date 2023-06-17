# python JSON 
import json 

z='{"name":"omkar","age":"18"}'
y=json.loads(z); print(y)

# result in dict 
print(y['age'])

# convert from python to json 

x={
    'name':'omkar',
    'age':18,
    'college':'bits pilani',
    'company':'atlassian'
}
y=json.dumps(x)

print(y)