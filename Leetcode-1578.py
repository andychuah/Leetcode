class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        n = len(colors)
        dp = [0] * (n + 1)
        previousColor = 'a'
        previousTime = 0

        for i in range(1, n + 1):
            if colors[i - 1] == previousColor:
                dp[i] = dp[i - 1] + min(neededTime[i - 1], previousTime)
                previousTime = max(neededTime[i - 1], previousTime)
            else:
                dp[i] = dp[i - 1]
                previousColor = colors[i - 1]
                previousTime = neededTime[i - 1]
            #print(dp, previousColor, previousTime)
        return dp[n]