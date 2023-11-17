class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        min_max_pair_sum = float('-inf')

        while left < right:
            current_pair_sum = nums[left] + nums[right]
            min_max_pair_sum = max(min_max_pair_sum, current_pair_sum)
            left += 1
            right -= 1

        return min_max_pair_sum