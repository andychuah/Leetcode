class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = defaultdict(list)
        for src, des in tickets:
            graph[src].append(des)
        
        for src in graph:
            graph[src].sort(reverse = True)
        
        stack = ['JFK']
        res = []
        
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            else:
                res.append(stack.pop())
        
        return res[::-1]