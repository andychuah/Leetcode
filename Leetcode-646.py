class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x: x[1])
        prev = pairs[0]
        res = 1

        for cur in pairs[1:]:
            if cur[0] > prev[1]:
                res += 1
                prev = cur

        return res