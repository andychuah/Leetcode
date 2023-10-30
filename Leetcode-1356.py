class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        binary = []
        for i in arr:
          bin_num = bin(i)[2:]
          binary.append(bin_num.count('1'))
        return [x for _ , x in sorted(zip(binary,arr))]