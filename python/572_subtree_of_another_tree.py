# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def is_same_tree(r1, r2):
            return (
                not r1 and not r2
                or (
                    r1 and r2
                    and r1.val == r2.val
                    and is_same_tree(r1.right, r2.right)
                    and is_same_tree(r1.left, r2.left)
                )
            )

        return is_same_tree(root, subRoot) or self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
