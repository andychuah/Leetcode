class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest, secondLargest = 0, 0
        smallest, secondSmallest = float('inf'), float('inf')

        for n in nums:
            if n < smallest:
                secondSmallest = smallest
                smallest = n
            elif n < secondSmallest:
                secondSmallest = n

            if n > largest:
                secondLargest = largest
                largest = n
            elif n > secondLargest:
                secondLargest = n

        return (largest * secondLargest) - (smallest * secondSmallest)
        '''
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]
        '''