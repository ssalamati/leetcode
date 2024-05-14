# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack, res = [root], []
        visited = [False]

        while stack:
            cur = stack.pop()
            v = visited.pop()
            if not v:
                stack.append(cur)
                visited.append(True)

                if cur.right:
                    stack.append(cur.right)
                    visited.append(False)

                if cur.left:
                    stack.append(cur.left)
                    visited.append(False)
            else:
                res.append(cur.val)
   
        return res
