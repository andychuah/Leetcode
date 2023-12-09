# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inOrder(node):
            if not node:
                return

            if node.left:
                inOrder(node.left)

            self.res.append(node.val)

            if node.right:
                inOrder(node.right)
                
        self.res = []
        inOrder(root)
        return self.res

        