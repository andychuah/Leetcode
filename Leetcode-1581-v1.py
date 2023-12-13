class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        # Runtime: 259ms
        def specialPosition(mat, row, col, n, m):
            cnt = 0
            for i in range(m):
                if mat[row][i] == 1:
                    cnt += 1
            for i in range(n):
                if mat[i][col] == 1:
                    cnt += 1
            return False if cnt > 2 else True

        m, n = len(mat), len(mat[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and specialPosition(mat, i, j, m, n):
                    res += 1
        return res
