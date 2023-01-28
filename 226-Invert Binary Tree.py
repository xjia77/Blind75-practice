# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        这道题是反转二叉树，运用了递归的思想，直到return none
        """
        if not root:
            return None

        tmp = root.right
        root.right = root.left
        root.left = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

