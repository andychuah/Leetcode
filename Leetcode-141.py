class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        first, second = head, head
        while first and second and second.next:
            first = first.next
            second = second.next.next
            if first == second:
                return True
        return False
