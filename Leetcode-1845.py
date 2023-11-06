class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.last = 0
        self.pq = []
        

    def reserve(self):
        """
        :rtype: int
        """
        if not self.pq:
            self.last += 1
            return self.last
        return heapq.heappop(self.pq)
        

    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        if seatNumber == self.last:
            self.last -= 1
        else:
            heapq.heappush(self.pq, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)