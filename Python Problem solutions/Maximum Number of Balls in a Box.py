class Solution(object):
    def digit_sum(self,num):
        s=0
        while num!=0:
            rem=num%10
            s=s+rem
            num=num//10
        return s
    #k= {}
    def countBalls(self, lowLimit, highLimit):
        k= {}
        for ball in range(lowLimit,highLimit+1):
            box = self.digit_sum(ball)               
            k[box] = k.get(box, 0) + 1 
        max_value = max(k.values())
        return max_value

# Example usage:
sol = Solution()
print(sol.countBalls(1, 10))  # Output: 2

    


        
        