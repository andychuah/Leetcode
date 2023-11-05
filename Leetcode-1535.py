class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # Runtime beats 100%
        # Memory beats 73.33%
        if k == 1:
            return max(arr[0], arr[1])
        if k >= len(arr):
            return max(arr)
        current_winner = arr[0]
        consecutive_wins = 0
        
        for i in range(1, len(arr)):
            if current_winner > arr[i]:
                consecutive_wins += 1
            else:
                current_winner = arr[i]
                consecutive_wins = 1
            
            if consecutive_wins == k:
                return current_winner
        return current_winner
        '''
        Runtime beats 26.67%
        Memory beats 73.33%
        if k == 1:
            return max(arr[0], arr[1])
        if k >= len(arr):
            return max(arr)
        win_tmp, win_count = -1, 1
        while(True):
            if arr[1] > arr[0]:
                arr.append(arr[0])
                del arr[0]
            else:
                arr.append(arr[1])
                del arr[1]
            if win_tmp != arr[0]:
                win_tmp = arr[0]
                win_count = 1
            else:
                win_count += 1

            if win_count == k:
                return arr[0]
        '''