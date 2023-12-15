class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        start_cities = set()

        for path in paths:
            start_cities.add(path[0])

        for path in paths:
            if path[1] not in start_cities:
                return path[1]
        return ""