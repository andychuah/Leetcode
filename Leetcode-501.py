# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.inOrderList = []
        def inOrder(root):
            if not root:
                return
            self.inOrderList.append(root.val)
            inOrder(root.left)
            inOrder(root.right)
        inOrder(root)
        freq = collections.Counter(self.inOrderList)
        maxx = max(freq.values())
        return [x for x in freq if freq[x] == maxx]