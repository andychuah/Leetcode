class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel_list = []
        vowel_index = []
        for index, char in enumerate(s):
            if char.lower() in {'a', 'e', 'i', 'o', 'u'}:
                vowel_list.append(char)
                vowel_index.append(index)
        vowel_list.sort()
        res = list(s)

        for i in range(len(vowel_list)):
            res[vowel_index[i]] = vowel_list[i]
        return ''.join(res)
        