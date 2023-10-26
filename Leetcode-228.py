class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
        elif len(nums) > 1:
            res,tmp = [], [str(nums[0])]
            for i in range(1,len(nums)):
                if nums[i] == nums[i-1] + 1:
                    tmp.append(str(nums[i]))
                else:
                    tmpStr = ""
                    if tmp[0] != tmp[-1]:
                        tmpStr = tmp[0] + "->" + tmp[-1]
                    else:
                        tmpStr = tmp[0]
                    res.append(tmpStr)
                    tmp = [str(nums[i])]
        tmpStr2 = ""
        if tmp[0] != tmp[-1]:
            tmpStr2 = tmp[0] + "->" + tmp[-1]
            res.append(tmpStr2)
        else:
            res.append(tmp[0])
        return res
                