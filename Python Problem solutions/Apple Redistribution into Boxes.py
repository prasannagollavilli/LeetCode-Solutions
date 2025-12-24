class Solution(object):
    def minimumBoxes(self, apple, capacity):
        capacity.sort()
        capacity=capacity[::-1]

        capacity_sum=0
        apple_sum=0
        k=0
        for i in apple:
            apple_sum=apple_sum+i
        #print(apple_sum)
        for j in range (len(capacity)):
            capacity_sum=capacity_sum+capacity[j]
            #print(capacity_sum)
            if capacity_sum>=apple_sum:
                k=j
                break    
        return k+1


            


        
        
        