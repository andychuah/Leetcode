class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, total, maxFreq = 0, 0, 0
        nums.sort()

        for right in range(len(nums)):
            total += nums[right]

            while total + k < nums[right] * (right - left + 1):
                total -= nums[left]
                left += 1
            maxFreq = max(maxFreq, right - left + 1)

        return maxFreq