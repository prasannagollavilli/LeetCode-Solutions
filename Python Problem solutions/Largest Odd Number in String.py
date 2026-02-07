class Solution(object):
    def largestOddNumber(self, num):
        str_num=int(num)
        while str_num!=0:
            rem=str_num%10
            if rem%2!=0:
                return str(str_num)
            str_num=str_num//10
        return ""