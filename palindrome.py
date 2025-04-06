class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        mylist=[]
        for i in range(len(x)-1,-1,-1):
            if x[i].isdigit():
                mylist.append(x[i])
        result="".join(mylist)
        if x == result:
            return True
        else:
            return False
