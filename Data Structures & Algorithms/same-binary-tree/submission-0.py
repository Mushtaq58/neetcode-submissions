# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        if (p is not None and q is None) or (p is None and q is not None):
            return False

        queue1 = deque([p])
        queue2 = deque([q])

        while queue1 and queue2:
            first_tree_node = queue1.popleft()
            second_tree_node = queue2.popleft()

            if first_tree_node.val != second_tree_node.val:
                return False

            if (first_tree_node.left is not None and second_tree_node.left is None) or (first_tree_node.left is None and second_tree_node.left is not None):
                return False
            elif first_tree_node.left is not None and second_tree_node.left is not None:
                queue1.append(first_tree_node.left)
                queue2.append(second_tree_node.left)

            if (first_tree_node.right is not None and second_tree_node.right is None) or (first_tree_node.right is None and second_tree_node.right is not None):
                return False
            elif first_tree_node.right is not None and second_tree_node.right is not None:
                queue1.append(first_tree_node.right)
                queue2.append(second_tree_node.right)

        return True