# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        while queue:
            curr_len = len(queue)
            max_val = float('-inf')

            for _ in range(curr_len):
                node = queue.popleft()
                max_val = max(max_val, node.val)

                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)

            result.append(max_val)
        return result
        