# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def preOrder(node):
            if not node:
                return
            self.ans += str(node.val)

            if node.left or node.right:
                self.ans += "("
                preOrder(node.left)
                self.ans += ")"
            
            if node.right:
                self.ans += "("
                preOrder(node.right)
                self.ans += ")"
        self.ans = ""
        preOrder(root)
        return self.ans
        
