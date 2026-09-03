# Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        old_to_new = {}

        def dfs(current):
            if current in old_to_new:
                return old_to_new[current]

            clone = Node(current.val)
            old_to_new[current] = clone

            for neighbor in current.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)