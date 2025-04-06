Input = "abc123xyz456"
Length=len(Input)
print(Length)
mylist=[]

for i in range(0,Length-1):
    if Input[i].isdigit() and Input[i+1].isdigit() :
        mylist.append(Input[i])
    elif Input[i].isdigit() and Input[i+1].isalpha() and Input[i+2].isalpha():
        mylist.append(Input[i])
        break
 
result = "".join(mylist)
print(result)
