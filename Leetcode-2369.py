class Solution(object):
    def validPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        dp = [False] * 3
        dp[0] = True

        for i in range(2, len(nums) + 1):
            ans = False

            if nums[i-1] == nums[i-2]:
                ans = ans or dp[(i-2)%3]

            if i>=3 and nums[i-1] == nums[i-2] == nums[i-3]:
                ans = ans or dp[(i-3)%3]

            if i>=3 and nums[i-1] == nums[i-2] + 1 == nums[i-3] + 2:
                ans = ans or dp[(i-3)%3]

            dp[i%3] = ans
        return dp[len(nums)%3]
