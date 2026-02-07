class Solution(object):
    def mirrorDistance(self, n):
        rev=0
        temp=n
        while n!=0:
            rem=n%10
            rev=rev*10+rem
            n=n//10
        return (abs(temp-rev))