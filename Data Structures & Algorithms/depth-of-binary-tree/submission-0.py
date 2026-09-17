# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return self.helper(root, 1)

    def helper(self, root, k):
        if root.left is None and root.right is None:
            return k

        left = k
        right = k

        if root.right is not None:
            right = self.helper(root.right, k + 1)
        if root.left is not None:
            left = self.helper(root.left, k + 1)
        return max(left, right)