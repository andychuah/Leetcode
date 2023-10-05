class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num, count in Counter(nums).items():
            if count > len(nums) // 3:
                res.append(num)
        return res