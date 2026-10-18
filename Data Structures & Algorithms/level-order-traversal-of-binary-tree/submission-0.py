# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        bfs_deque = deque([root])
        tree_list = []

        while bfs_deque:
            level_list = []
            n = len(bfs_deque)

            for i in range(n):
                current_node = bfs_deque.popleft()

                level_list.append(current_node.val)

                if current_node.left:
                    bfs_deque.append(current_node.left)
                if current_node.right:
                    bfs_deque.append(current_node.right)

            tree_list.append(level_list)

        return tree_list