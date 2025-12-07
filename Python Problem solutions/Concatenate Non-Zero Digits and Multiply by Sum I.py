class Solution(object):
    def sumAndMultiply(self, n):
        temp=n
        k=str(n)
        y=k.replace("0","")
        sum=0
        while n!=0:
            rem=n%10
            sum=sum+rem
            n=n//10
        
        if temp!=0:
            return int(y)*sum
        else:
            return 0
        