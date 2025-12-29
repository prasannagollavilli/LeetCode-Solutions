class Solution(object):
    def majorityElement(self, nums):
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ans = max(d, key=d.get)
        return ans

        