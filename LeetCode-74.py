class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        result = False
        for i in matrix:
            for j in i:
                if(target == j):
                    result = True

        return result