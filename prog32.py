username=input()
print("username is: "+username)

tup1=()
n=int(input("entre number of elements"))

for i in range(n):
    ele=int(input())
    list1=list(tup1)
    list1.append(ele)
    tup1=tuple(list1)
print(tup1)

# list1=[]
# n=int(input("enter number of elements: "))
# for i in range(n):
#     ele=int(input())
#     list1.add(ele)
# print(list1)

# using try catch 
try:
    my_list=[]
    while True:
        my_list.append(int(input()))
except:
    print(my_list)