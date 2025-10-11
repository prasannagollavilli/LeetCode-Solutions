class Solution(object):
    def alternateDigitSum(self, n):
        lis=[]
        while n!=0:
            rem=n%10
            lis.append(rem)
            n=n//10
        lis=lis[::-1]
        print(lis)

        for i in range(1,len(lis),2):
            lis[i]=-1*lis[i]
        return sum(lis)
if __name__ == "__main__":
    sol = Solution()
    print(sol.alternateDigitSum(521))  # Example usage --- IGNORE ---