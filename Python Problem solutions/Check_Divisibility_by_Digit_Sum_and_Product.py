class Solution(object):
    def checkDivisibility(self, n):
        s=0
        p=1
        temp=n
        while n!=0:
            rem=n%10
            s=s+rem
            p=p*rem
            n=n//10
        return True if temp%(s+p)==0 else False
if __name__ == "__main__":
    sol = Solution()
    print(sol.checkDivisibility(99))  # Example usage --- IGNORE ---   