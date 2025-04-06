class Solution(object):
    def myAtoi(self, s):
        s=s.strip()

        if not s:
            return 0
        negative=False
        i=0
        if s[i]=='-':
            negative=True
            i=i+1
        elif s[i]=='+':
            i=i+1
        out=0
        while i < len(s) and s[i].isdigit():
            out = out * 10 + int(s[i])

            if not negative and out >= 2147483647:
                return 2147483647
            if negative and out > 2147483648:
                return -2147483648
            i+=1    
        if negative :
            return -out
        else:
            return out
