class Solution(object):
    def getLeastFrequentDigit(self, n):
        lis=[]
        while n!=0:
            rem=n%10
            lis.append(rem)
            n=n//10
        
        my_map = {}
        for i in lis:
            my_map[i] = lis.count(i)
       
        min_freq = min(my_map.values())
        least_digits = [k for k, v in my_map.items() if v == min_freq]
        return min(least_digits)
if __name__ == "__main__":
    sol = Solution()
    print(sol.getLeastFrequentDigit(123223))  # Example usage --- IGNORE ---