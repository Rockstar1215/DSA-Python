Input="12233542"
length=len(Input)
print()
mylist=[]
for i in range(length-1):
    a = int(Input[i])
    b = int(Input[i+1])
    mylist.append(Input[i])
    if a % 2 == 0 and b % 2 ==0:
        mylist.append("+")
    elif a % 2 == 1 and b % 2 == 1:
        mylist.append("-")
mylist.append(Input[-1])


result= "".join(mylist)
print(result)

