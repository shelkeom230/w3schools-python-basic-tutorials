# try except 
'''
try block lets you handle the code which can throw an error 
except block handles the exception
else block executes the code when there is no error 
finally block lets you execute code, regardless of the result of the try-except blocks
'''

try:
    x=10
    print(x)
except NameError:
    print("x not defined")
except: 
    print("something else went wrong, syntax error")

try:
    print("hello")
except:
    print("something went wrong")
else:
    print("nothing went wrong, execution done")
finally:
    print("i love python")

try:
    f=open("file.txt")
    try:
        f.write("omkar shelke")
    except:
        print(f.name," is not writable")
    finally:
        f.close()
except:
    print("something went wrong when opening file")

# x=-1
# if x<0:
#     raise Exception("sorry, no numbers below 0")

x="hello"
if not type(x) is int:
    raise TypeError("only integers are allowed")