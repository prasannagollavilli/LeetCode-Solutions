class Solution(object):
    def sortedSquares(self, nums):
        pos=[]
        neg=[]
        res=[]
        j=0
        k=0
        for i in nums:
            if i>=0:
                pos.append(i*i)
            else:
                neg.append(i*i)
        neg=neg[::-1]
        #print(neg)
        if len(pos)==0:
            return neg
        elif len(neg)==0:
            return pos
        else:
            while j<len(neg) and k<len(pos):
                if neg[j]<=pos[k]:
                    res.append(neg[j])
                    j=j+1
                else:
                    res.append(pos[k])
                    k=k+1
            while j<len(neg):
                res.append(neg[j])
                j=j+1
            while k<len(pos):
                res.append(pos[k])
                k=k+1
            return res

            

        
        