# file handling 

'''
file modes:
r- read mode
x- crate file
w- write mode
a- append mode
r+-read and write mode
w+- write and read mode
t- text-by default. text mode.
b- binary mode (e.g images)
'''

f=open("file.txt","r")
for x in f:
    print(x)

# write to an existing file 
with open("file1.txt","a") as f:
    f.write("omkar shelke\nsoftware engineer")

# import os
# os.remove('file1.txt')

# check if file exists 
import os 
if os.path.exists('file.txt'):
    print("file exists")
else:
    print("file not exists")

# to remove the folder use rmdir method 