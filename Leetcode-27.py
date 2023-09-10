class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        counter = 0
        res = []
        for i in range(len(nums)):
            if(val != nums[i]):
                counter += 1
            else:
                nums[i] = '_'
        nums.sort()
        return counter
        '''
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == val:
                del nums[i]
                n -= 1
            else:
                i += 1
        return len(nums)
        #20ms
        ''' 