class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        k=""
        for i in s:
            if i.isalnum():
                k=k+i
        return True if k==(k[::-1]) else False
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # Example usage --- IGNORE ---