class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        lis=[]
        for k in range(len(nums)-2):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i=k+1
            j=len(nums)-1
            while i<j:
                if nums[i]+nums[j]==-nums[k]:
                    lis.append([nums[k],nums[i],nums[j]])
                    i=i+1
                    j=j-1
                    while(i<j and nums[i]==nums[i-1]):
                        i=i+1
                    while(i<j and nums[j]==nums[j+1]):
                        j=j-1
                elif nums[i]+nums[j]<-nums[k]:
                    i=i+1
                else:
                    j=j-1
        return lis
        print(lis)