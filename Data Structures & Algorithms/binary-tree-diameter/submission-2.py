# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def height_using_postorder(node):
            if not node:
                return 0

            left = height_using_postorder(node.left)
            right = height_using_postorder(node.right)

            height = 1 + max(left, right)
            self.diameter = max(self.diameter, left+right)

            return height

        height_using_postorder(root)
        return self.diameter


"""
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def height_using_postorder(node):
            if not node:
                return 0

            left_height = height_using_postorder(node.left)
            right_height = height_using_postorder(node.right)
            
            height = 1 + max(left_height, right_height)
            self.diameter = max(self.diameter, left_height + right_height)

            return height

        height_using_postorder(root)
        return self.diameter
"""