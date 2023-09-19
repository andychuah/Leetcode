class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nList = [0] * n

        for i in nums:
            nList[i] += 1

        for i in range(len(nList)):
            if nList[i] > 1:
                return i