class Solution(object):
    def even(self,num):
        num=num//2
        return num
    def odd(self, num):
        num=num-1
        return num
    def numberOfSteps(self, num):
        c=0
        while num!=0:
            if num%2==0:
                k=self.even(num)
                c=c+1
                num=k
            else:
                y=self.odd(num)
                c=c+1
                num=y
        return c
        
        