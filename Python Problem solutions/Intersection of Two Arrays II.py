class Solution(object):
    def intersect(self, nums1, nums2):
        '''#brute force
        lis=[]
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                lis.append(i)

        return lis'''
        #Optimized-Two pointers
        nums1.sort()
        nums2.sort()
        lis=[]
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                lis.append(nums1[i])
                i=i+1
                j=j+1
            elif nums1[i]<nums2[j]:
                i=i+1
            else:
                j=j+1
        return lis