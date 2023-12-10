class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(n):
            tmpList = []
            for j in range(m):
                tmpList.append(matrix[j][i])
            res.append(tmpList)
        return res
        