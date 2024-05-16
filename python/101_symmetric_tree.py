# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.compare(root.left, root.right)

    def compare(self, n1, n2):
        if not n1 and not n2:
            return True

        return n1 and n2 and n1.val == n2.val and self.compare(n1.left, n2.right) and self.compare(n1.right, n2.left)
