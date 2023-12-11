class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr) // 4
        occur, tmpNum = 0, arr[0]
        for i in arr:
            if i == tmpNum:
                occur += 1
            else:
                tmpNum = i
                occur = 1
            if occur > n:
                return i