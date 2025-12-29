import math
class Solution(object):
    def judgeSquareSum(self, c):
        lis=[]
        for i in range(int(math.sqrt(c))+1):
            lis.append(i*i)
        #print(lis)
        i=0
        j=len(lis)-1
        while i<=j:
            if lis[i]+lis[j]==c:
                return True
            elif lis[i]+lis[j]<c:
                i=i+1
            else:
                j=j-1
        return False
        