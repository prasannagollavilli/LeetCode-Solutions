class Solution(object):
    def singleNumber(self, nums):
        k=sum(set(nums))
        f=sum(nums)
        return 2*k-f


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [4, 1, 2, 1, 2]
    result = solution.singleNumber(nums)
    print("The single number is:", result)