class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums) # get required number of rotations
        nums[::] = nums[len(nums)-k:] + nums[0:len(nums)-k]  # change inplace
                
        