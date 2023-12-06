class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        week_count = n // 7
        remaining_days = n % 7
        
        total = ((week_count * (week_count - 1)) // 2) * 7 
        total += week_count * 28
        total += ((remaining_days * (remaining_days + 1)) // 2) + (week_count * remaining_days)
        
        return total
        '''
        Slower solution
        res, start = 0, 1
        div, mod = n / 7, n % 7
        
        for i in range(div):
            for j in range(start, start+7):
                res = res + j
            start += 1
        for i in range(start, start+mod):
            res += i
        return res
'''