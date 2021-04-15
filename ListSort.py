
UserList: list = []
NewList: list = []

n = int(input("Please enter the number of elements of the list followed by the elements :\n"))

for i in range(0,n):
    ele = int(input())

    UserList.append(ele)
print("The given list is :\n" , UserList)
for i in range(0,n):
    if UserList[i] > 0:
        NewList.append(UserList[i])

print("The positive elements are :\n" ,NewList)
