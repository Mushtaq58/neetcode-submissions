# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def postorder(node):
            if not node:
                return 0

            left = postorder(node.left)
            right = postorder(node.right)

            height = 1 + max(left, right)
            self.diameter = max(self.diameter, left+right)

            return height

        postorder(root)
        return self.diameter