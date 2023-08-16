class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 1:
            return nums
        
        deq = deque()
        
        result = []
        for i in range(len(nums)):
            while deq and deq[0] < i - k + 1:
                deq.popleft()
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
            
            deq.append(i)
            if i >= k - 1:
                result.append(nums[deq[0]])
        
        return result

        # Time limit exceeded
        #sliceStart = 0
        #for i in range(k,len(nums)+1):
        #    dpTemp = nums[sliceStart:i]
        #    dp.append(max(dpTemp))
        #    sliceStart += 1
        return dp