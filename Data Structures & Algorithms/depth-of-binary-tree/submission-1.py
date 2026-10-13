# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)

        """
        if root is none:
            return 0

        depth = 1

        tree_stack = [(root, depth)]
        max_depth = 1

        while tree_stack:
            current_node, depth = tree_stack.pop()

            max_depth = max(max_depth, depth)

            depth = depth + 1

            if current_node.left is not None:
                tree_stack.append((current_node.left, depth))
            if current_node.right is not None:
                tree_stack.append((current_node.right, depth))

        return max_depth
        """