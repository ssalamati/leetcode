# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        return (
            (not root.right and not root.left and root.val == targetSum)
            or self.hasPathSum(root.right, targetSum - root.val)
            or self.hasPathSum(root.left, targetSum - root.val)
        )
