class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = [0] * 26
        for character in s:
            freq[ord(character)-ord('a')] += 1
        freq.sort()

        del_count = 0
        for i in range(24,-1,-1):
            if freq[i] == 0:
                break
            
            if freq[i] >= freq[i+1]:
                prev = freq[i]
                freq[i] = max(0,freq[i+1] - 1) #The smallest frequency is 0
                del_count += prev - freq[i]
            
        return del_count
        