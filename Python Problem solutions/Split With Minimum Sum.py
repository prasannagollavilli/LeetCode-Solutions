class Solution(object):
    def splitNum(self, num):
        lis=[]
        while num!=0:
            k=num%10
            lis.append(k)
            num=num//10
        lis.sort()
        
        num1=0
        num2=0
        for i in range(0,len(lis),2):
            num1=num1*10+lis[i]
        for i in range(1,len(lis),2):
            num2=num2*10+lis[i]
        return num1+num2