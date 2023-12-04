class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        maxNum = -1
        for i in range(1, len(num)-1):
            if num[i-1] == num[i] and num[i] == num[i+1] and num[i] > maxNum:
                maxNum = num[i]
        return maxNum*3 if maxNum != -1 else ""
        