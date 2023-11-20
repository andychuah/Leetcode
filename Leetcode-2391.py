class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        hasG, hasP, hasM = False, False, False
        n = len(garbage)
        total_time = 0

        for i in range(n-1):
            total_time += 3 * travel[i]

        for i in range(n):
            total_time += len(garbage[i])
        
        for i in range(n-1, 0 ,-1):
            if 'G' not in garbage[i]:
                total_time -= travel[i-1]
            else:
                break
        for i in range(n-1, 0 ,-1):
            if 'P' not in garbage[i]:
                total_time -= travel[i-1]
            else:
                break
        for i in range(n-1, 0 ,-1):
            if 'M' not in garbage[i]:
                total_time -= travel[i-1]
            else:
                break    
        return total_time