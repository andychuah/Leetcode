class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        def isArithmetic(arr):
            arr.sort()
            diff = arr[1] - arr[0]

            for i in range(2, len(arr)):
                if arr[i] - arr[i - 1] != diff:
                    return False
            return True

        ans= []
        for i in range(len(l)):
            arr = nums[l[i] : r[i] + 1]
            ans.append(isArithmetic(arr))
        return ans