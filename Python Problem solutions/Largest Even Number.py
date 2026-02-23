class Solution(object):
    def largestEven(self, s):
        for i in range(len(s)-1,-1,-1):
            if int(s[i])!=2:
                s=s[:-1]
            else:
                return s
        return ""
