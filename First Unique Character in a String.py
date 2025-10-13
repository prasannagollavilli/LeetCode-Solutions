class Solution(object):
    def firstUniqChar(self, s):
        s_map={}
        for ch in s:
            s_map[ch] = s_map.get(ch, 0) + 1

        for i in range(len(s)):
            if s_map[s[i]]==1:
                return i
        return -1
if __name__ == "__main__":
    sol = Solution()
    print(sol.firstUniqChar("leetcode"))  # Example usage --- IGNORE ---