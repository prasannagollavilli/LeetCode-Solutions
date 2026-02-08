class Solution(object):
    def isFascinating(self, n):
        n2=2*n
        n3=3*n
        
        str1=str(n)+str(n2)+str(n3)
        #print(str1)
        #print(Final_num)

        if len(str1)==9 and set(str1)==set("123456789"):
            return True
        return False
        


        