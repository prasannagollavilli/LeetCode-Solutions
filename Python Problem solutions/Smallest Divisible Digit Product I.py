class Solution(object):
    def digitprod(self,n):
        s=1
        while n!=0:
            s=s*(n%10)
            n=n//10
        return s

    def smallestNumber(self, n, t):
        for i in range(n,n+10):
            if self.digitprod(i)%t==0:
                return i

        