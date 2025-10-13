class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for char in set(ransomNote):
            if magazine.count(char)<ransomNote.count(char):
                    return False
        return True
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.canConstruct("a","b"))  # Example usage --- IGNORE ---