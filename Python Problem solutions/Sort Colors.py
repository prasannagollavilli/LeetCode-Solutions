class Solution(object):
    def sortColors(self, nums):
       zero=0
       one=0
       two=0
       for i in nums:
        if i==0:
            zero=zero+1
        elif i==1:
            one=one+1
        else:
            two=two+1
       nums[:] = []
       for i in range(zero):
        nums.append(0)
       for i in range(one):
        nums.append(1)
       for i in range(two):
        nums.append(2)
       return nums
    

