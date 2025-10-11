class Solution(object):
    def get_num(self,li):
        result = int(''.join(str(x) for x in li))
        return result

    def flip_num(self,num):
        return 9 if num==6 else 6

    def maximum69Number (self, num):
        lis=[]
        while num!=0:
            rem=num%10
            lis.append(rem)
            num=num//10
        lis = lis[::-1]
        m=self.get_num(lis)
        for i in range(0,len(lis)):
            temp = lis[:]  # Make a copy
            temp[i] = self.flip_num(temp[i])
            s = self.get_num(temp)
            m = max(s, m)
        return m
if __name__ == "__main__":
    sol = Solution()
    print(sol.maximum69Number(666999))
