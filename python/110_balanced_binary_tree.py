# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
    
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal balanced
            if not root:
                return 0

            r = dfs(root.right)
            l = dfs(root.left)

            if abs(r - l) > 1:
                balanced = False

            return max(r, l) + 1

        dfs(root)

        return balanced
        