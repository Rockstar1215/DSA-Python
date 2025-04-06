class Solution(object):
    def areNumbersAscending(self, s):
        length=len(s)
        mylist=[]
        num=""
        for i in range(length):
            if s[i].isdigit():
                num+=s[i]
            elif num:
                mylist.append(num)
                num=""
        if num:
            mylist.append(num)

        s=[int(n) for n in mylist]

        for i in range(0,len(s)-1):
            a= int(s[i])
            b= int(s[i+1])

            if a>=b:
                return False
                break
        else:
            return True

                
