class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        # Runtime: 8ms , beats 94.69%
        visited = [(0,0)]
        for direction in path:
            if direction == 'N':
                lastVisit = visited[-1]
                currVisit = (lastVisit[0], lastVisit[1] + 1)
                if currVisit in visited:
                    return True
                else:
                    visited.append(currVisit)
            elif direction == 'S':
                lastVisit = visited[-1]
                currVisit = (lastVisit[0], lastVisit[1] - 1)
                if currVisit in visited:
                    return True
                else:
                    visited.append(currVisit)
            elif direction == 'E':
                lastVisit = visited[-1]
                currVisit = (lastVisit[0] + 1, lastVisit[1])
                if currVisit in visited:
                    return True
                else:
                    visited.append(currVisit)
            elif direction == 'W':
                lastVisit = visited[-1]
                currVisit = (lastVisit[0] - 1, lastVisit[1])
                if currVisit in visited:
                    return True
                else:
                    visited.append(currVisit)
        return False