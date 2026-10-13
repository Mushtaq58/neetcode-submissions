# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        left_inverted = self.invertTree(root.left)
        right_inverted = self.invertTree(root.right)

        root.left = right_inverted
        root.right = left_inverted

        return root

        """
        if root is None:
            return None

        queue = [root]

        while queue:
            current = queue.pop(0)

            current.left, current.right = current.right, current.left

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return root
        """

        """
        from collections import deque

        def invertTree(self, root):
            if root is None:
                return None

            queue = deque([root])

            while queue:
                current = queue.popleft()  # This is a better approach because queue.pop(0) takes O(n) time due to element shifting. deque (double-ended queue) is better because it performs popleft() in O(1) time. It doesn't shift the remaining elements; it efficiently adds or removes elements at either end, changing the queue length.

                current.left, current.right = current.right, current.left

                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)

            return root
        """

        