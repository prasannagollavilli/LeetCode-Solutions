class Solution(object):
    def xorOperation(self, n, start):
        lis=[]
        for i in range(n):
            lis.append(start+2*i)
        k=0
        for j in lis:
            k=k^j
        return k
if __name__ == "__main__":
    sol = Solution()
    print(sol.xorOperation(5, 0))  # Example usage