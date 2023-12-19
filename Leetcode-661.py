class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        def calImage(img, x, y):
            total, count = 0, 0
            m, n = len(img), len(img[0])
            for i in range(max(0, x-1), min(x+2, m)):
                for j in range(max(0, y-1), min(y+2, n)):
                    total += img[i][j]
                    count += 1
            return total // count
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                result[i][j] = calImage(img, i, j)
        return result