class Solution(object):
    def removeZeros(self, n):
        k=str(n)
        k=k.replace('0','')
        return int(k)
if __name__ == "__main__":
    sol = Solution()
    print(sol.removeZeros(102030))  # Example usage