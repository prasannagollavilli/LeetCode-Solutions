class Solution(object):
    def countPartitions(self, nums):
        tsum=sum(nums)
        lsum=0
        c=0
        for i in range(len(nums)-1):
            lsum=lsum+nums[i]
            rsum=tsum-lsum
            if (lsum-rsum)%2==0:
                c=c+1
        return c
if __name__ == "__main__":
    sol = Solution()
    print(sol.countPartitions([10,10,3,7,6]))  # Example usage --- IGNORE ---