class Solution(object):
    def reverse(self, x):
        x=str(x)
        mylist=[]
        min_x= -2**31
        max_x= 2**31 - 1
        sign = ""
        for i in range(0, len(x)):
            if x[i] == '-':
               sign="-"
            elif x[i].isdigit():
                mylist.append(x[i])
        result="".join(reversed(mylist))
        result =int(sign+result)

        if result < min_x or result > max_x:
            return 0
        else:

            return result
