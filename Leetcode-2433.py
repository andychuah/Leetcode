class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        result = [pref[0]]
        for i in range(1,len(pref)):
            result.append(pref[i] ^ pref[i-1])
        return result