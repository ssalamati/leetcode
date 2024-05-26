"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        nodes = {}

        def dfs(inp_node):
            if inp_node.val in nodes:
                return nodes[inp_node.val]

            new_node = Node(val=inp_node.val)
            nodes[inp_node.val] = new_node

            for neighbor in inp_node.neighbors:
                new_node.neighbors.append(dfs(neighbor))

            return new_node

        return dfs(node)
