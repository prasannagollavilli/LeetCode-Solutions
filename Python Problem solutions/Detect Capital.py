class Solution(object):
    def detectCapitalUse(self, word):
        if word.isupper() or word.islower():
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        return False
if __name__ == "__main__":
    sol = Solution()
    print(sol.detectCapitalUse("USA"))  # Example usage --- IGNORE ---
