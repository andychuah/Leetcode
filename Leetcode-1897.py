class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        if len(words) == 1:
            return True
        frequency = [0] * 26
        for word in words:
            for c in word:
                frequency[ord(c) - ord('a')] += 1
        
        for freq in frequency:
            if freq % len(words) != 0:
                return False
        return True
        