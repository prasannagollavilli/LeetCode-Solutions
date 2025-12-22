class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        if k<=numOnes:
            return k
        elif numOnes<k and k<=numOnes+numZeros:
            return numOnes
        elif k>numOnes+numZeros+numNegOnes or k<=numOnes+numZeros+numNegOnes:
            return (numOnes*1)+(k-numZeros-numOnes)*(-1)
        else:
            return 0
        