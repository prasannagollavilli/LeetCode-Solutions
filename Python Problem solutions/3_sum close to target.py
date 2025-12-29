class Solution:
    def countTriplets(self, n, sum, arr):
        ans=0
        arr.sort()
        for k in range(n-2):
            i=k+1
            j=n-1
            while i<j:
                s=arr[k]+arr[i]+arr[j]
                if s>=sum:
                    j=j-1
                else:
                    ans=ans+(j-i)
                    i=i+1
        return ans