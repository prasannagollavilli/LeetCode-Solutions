class Solution(object):
    def countDigits(self, num):
        temp=num
        c=0
        while num>0:
            rem=num%10
            if temp%rem==0:
                c=c+1
            num=num//10
        return c
if __name__ == "__main__":
    sol = Solution()
    print(sol.countDigits(121))  # Example usage --- IGNORE ---