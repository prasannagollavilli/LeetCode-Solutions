class Solution(object):
    def findClosest(self, x, y, z):
        x1=abs(z-x)
        y1=abs(z-y)
        if x1==y1:
            return 0
        elif x1<y1:
            return 1
        else:
            return 2