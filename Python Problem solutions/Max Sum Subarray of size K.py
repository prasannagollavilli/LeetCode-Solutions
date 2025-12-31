class Solution:
    def maxSubarraySum(self, arr, k):
        s=0
        for i in range(0,k):
            s=s+arr[i]
        #print(s)
        left=0
        right=k-1
        res=s
        while right<len(arr)-1:
            right=right+1
            left=left+1
            s=s+arr[right]-arr[left-1]
            res=max(res,s)
        return res
            
            