class Solution(object):
    def digit_sum(self,num):
        s=0
        while num!=0:
            rem=num%10
            s=s+rem
            num=num//10
        return s

    def differenceOfSum(self, nums):
        s=sum(nums)
        ds=0
        for i in nums:
            ds=ds+self.digit_sum(i)
        return abs(s-ds)
if __name__ == "__main__":
    sol = Solution()
    print(sol.differenceOfSum([1,15,6,3]))  # Example usage --- IGNORE ---

        