# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []
        self.dfs(root, res)
        return "".join(res)

    def dfs(self, root, res):
        if not root:
            return

        res.append(str(root.val))

        if not root.left and not root.right:
            return

        res.append("(")
        self.dfs(root.left, res)
        res.append(")")

        if root.right:
            res.append("(")
            self.dfs(root.right, res)
            res.append(")")
