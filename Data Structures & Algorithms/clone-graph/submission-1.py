# Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}

        oldToNew[node] = Node(node.val)

        queue = deque([node])

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                oldToNew[curr].neighbors.append(oldToNew[neighbor])

        return oldToNew[node]

    """
    from collections import deque
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}

        oldToNew[node] = Node(node.val)

        queue = deque([node])

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                oldToNew[curr].neighbors.append(oldToNew[neighbor])

        return oldToNew[node]

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        old_to_new = {}

        def dfs(current):

            if current not in old_to_new:
                return old_to_new[currnt]

            clone = Node(current.val)
            old_to_new[current] = clone

            for neighbor in current.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return (node)

    """