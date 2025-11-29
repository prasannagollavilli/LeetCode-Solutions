class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        temp=x
        lis=[]
        while x!=0:
            rem=x%10
            lis.append(rem)
            x=x//10
        s=0
        for i in lis:
            s=s+i

        return s if temp%s==0 else -1
    #print(self.sumOfTheDigitsOfHarshadNumber(18))
if __name__ == "__main__":
    sol = Solution()
    print(sol.sumOfTheDigitsOfHarshadNumber(18))  # Example usage --- IGNORE ---
    