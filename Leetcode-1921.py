class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        n = len(dist)
        time = [float(d) / s for d, s in zip(dist, speed)]
        time.sort()
        
        curr = 0
        for i in range(n):
            if time[i] <= i:
                break
            curr += 1
        
        return curr

        