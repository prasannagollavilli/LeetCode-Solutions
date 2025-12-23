class Solution(object):

    def threeSumClosest(self, nums, target):
        nums.sort()
        mx_diff=float("inf")
        res=0
        for k in range(len(nums)-2):
            i=k+1
            j=len(nums)-1
            while i<j:
                s=nums[k]+nums[i]+nums[j]
                if mx_diff>abs(target-s):
                    mx_diff=abs(target-s)
                    res=s
                if s==target:
                    return res
                    i=i+1
                    j=j-1
                elif s<target:
                    i=i+1
                else:
                    j=j-1
        return res

        
        