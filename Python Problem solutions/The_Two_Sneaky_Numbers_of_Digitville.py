class Solution(object):
    def getSneakyNumbers(self, nums):
        lis=set()
        for i in nums:
            if nums.count(i)>1:
                lis.add(i)
        
        k=list(lis)
        return k
if __name__ == "__main__":
    sol = Solution()
    print(sol.getSneakyNumbers([1,2,3,1,1,3,3,4,5,5]))  # Example usage --- IGNORE ---