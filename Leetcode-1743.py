class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        pairs = defaultdict(list)

        for val in adjacentPairs:
            pairs[val[0]].append(val[1])
            pairs[val[1]].append(val[0])

        result = []
        start, left = -1000000, -1000000

        for val in pairs:
            if(len(pairs[val]) == 1):
                start = val
                break
        result.append(start)

        for i in range(1, len(adjacentPairs) + 1):
            val = pairs[start]
            newval = val[0] if val[0] != left else val[1]
            result.append(newval)
            left = start
            start = newval
        
        return result