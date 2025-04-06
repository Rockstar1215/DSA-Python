class Solution(object):
    def checkString(self, s):
        s_len=len(s)
        mylist=[]
        for i  in range(s_len):
            if s[i]=='a'or s[i]=='b':
                mylist.append(s[i])
        for i in range(len(mylist)-1):
            if mylist[i]=='b' and mylist[i+1]=='a':
                return False
        return True
