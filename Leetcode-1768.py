class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result, i = [], 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1
        return ''.join(result)

        '''
        res = ""
        ptr1, ptr2= 0, 0
        while(ptr1 < len(word1)):
            res += word1[ptr1]
            ptr1 += 1
            if len(word2) > len(word1) and ptr1 == len(word1) and ptr2 != len(word2):
                while ptr2 < len(word2):
                    res += word2[ptr2]
                    ptr2 += 1
            while(ptr2 < len(word2)):
                res += word2[ptr2]
                ptr2 += 1
                break
        return res
        '''