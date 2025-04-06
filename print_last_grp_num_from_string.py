Input = "abc123xyz456asa"
Length=len(Input)
print(Length)
mylist=[]

for i in range(Length-1,1,-1):
    if Input[i].isdigit() and Input[i-1].isdigit() :
        mylist.append(Input[i])
    elif Input[i].isdigit() and Input[i-1].isalpha() and Input[i-2].isalpha():
        mylist.append(Input[i])
        break
 
result = "".join(reversed(mylist))
print(result)
