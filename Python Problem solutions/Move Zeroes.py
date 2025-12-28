class Solution(object):
    def moveZeroes(self, nums):
        pos=0
        temp=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[pos]=nums[i]
                pos=pos+1
        for i in range(pos,len(nums)):
            nums[i]=0
        return nums
        

            
        