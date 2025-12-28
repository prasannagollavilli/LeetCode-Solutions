class Solution(object):
    def countNegatives(self, grid):
        """c=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]<0:
                    c=c+1
        return c"""
        c=0
        for i in grid:
            left=0
            right=len(i)-1
            
            while left<=right:
                mid=(left+right)//2
                if i[mid]<0:
                    right = mid - 1
                else:
                    left=mid+1
            c+= (len(i) - left)
        return c



