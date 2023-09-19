class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        soldierList = []
        for subList in mat:
            soldier = 0
            for i in subList:
                if i == 1:
                    soldier += 1
            soldierList.append(soldier)
        res = []
        for i in range(k):
            minVal = min(soldierList)
            res.append(soldierList.index(minVal))
            soldierList[soldierList.index(minVal)] = 100

        return res
        