class Solution(object):
    def maxProduct(self, n):
        lis=[]
        while n!=0:
            rem=n%10
            lis.append(rem)
            n=n//10
        lis.sort()
        return lis[-1]*lis[-2]
        
        
        