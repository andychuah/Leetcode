class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        numsCombine = []
        numsCombine = nums1 + nums2
        numsCombine = sorted(numsCombine)

        res, n = 0.0000, len(numsCombine)
        #Even 
        if(n % 2 != 0):
            res = numsCombine[(n / 2)]
        elif(n % 2 == 0):
            res = (numsCombine[(n/2)-1] + numsCombine[(n/2)]) / 2.0
        return res
        