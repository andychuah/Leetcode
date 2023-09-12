class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, majority = 0, 0

        for i in range(len(nums)):
            if count == 0 and nums[i] != majority:
                majority = nums[i]
                count += 1
            elif majority == nums[i]:
                count += 1
            else:
                count -= 1
        return majority