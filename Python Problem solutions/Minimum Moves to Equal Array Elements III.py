class Solution(object):
    def minMoves(self, nums):
        m=max(nums)
        c=0
        for i in nums:
            c=c+(m-i)
        return c