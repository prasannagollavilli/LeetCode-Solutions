class Solution(object):
    def digit(self, num):
        s=0
        while num!=0:
            rem=num%10
            s=s+rem
            num=num//10
        return s

    def smallestIndex(self, nums):
        #print(self.digit(233))
        for i in range(len(nums)):
            if self.digit(nums[i])==i:
                return i
        return -1
            
        
        