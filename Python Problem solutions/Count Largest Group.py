class Solution(object):
    def digitsum(self,n):
        s=0
        while n!=0:
            s=s+(n%10)
            n=n//10
        return s
    def countLargestGroup(self, n):
        d={}
        for i in range(1,n+1):
            s = self.digitsum(i)
            if s not in d:
                d[s] = []
            d[s].append(i)

        max_size=0
        for v in d.values():
            if len(v)>max_size:
                max_size=len(v)
        c=0
        for v in d.values():
            if max_size==len(v):
                c=c+1
        return c

        