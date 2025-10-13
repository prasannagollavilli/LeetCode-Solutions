class Solution(object):
    def reverseString(self, s):
        left=0
        right=len(s)-1
        temp=''
        while left<right:
            temp=s[left]
            s[left]=s[right]
            s[right]=temp
            left=left+1
            right=right-1
        return s
if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseString(["h","e","l","l","o"]))  # Example usage --- IGNORE ---