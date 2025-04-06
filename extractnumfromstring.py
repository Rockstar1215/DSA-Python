Input = "abc123xyz"
Length=len(Input)
print(Length)
mylist=[]
i=0
for i in range(i,Length-1):
    if Input[i].isnumeric():
        mylist.append(Input[i])
    else:
        i=i+1
        
print(mylist)

result= "".join(mylist)
print(result)
