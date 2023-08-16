class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsMap = {}
        for i in range(len(nums)):
            if target - nums[i] in numsMap:
                return [numsMap[target - nums[i]], i]
            numsMap[nums[i]] = i
        return []

        # O(n^2)
        #for i in range(len(nums)):
        #    for j in range(i+1,len(nums)):
        #        if nums[i] + nums[j] == target:
        #            return [i,j]