# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.result = 0
        def postorder(node):
            if not node:
                return (0,0)
            
            left = postorder(node.left)
            right = postorder(node.right)

            total_sum = left[0] + right[0] + node.val
            total_cnt = 1 + left[1] + right[1]
            self.result += (node.val == total_sum / total_cnt)
            return (total_sum, total_cnt)

        postorder(root)
        return self.result
        