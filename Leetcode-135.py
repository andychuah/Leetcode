class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candies = [1] * n # Everyone has at least one candy

        # Compare with previous child, if ratings higher, give one more candy
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        # Compare with next child, if ratings higher, give one more candy
        for i in range(n-2 , -1 , -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i] , candies[i+1] + 1)

        return sum(candies)

        