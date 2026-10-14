# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque([root])

        while queue:
            current_root = queue.popleft()

            if current_root.val == subRoot.val:
                ans = self.isSameTree(current_root, subRoot)

                if ans is True:
                    return True

            if current_root.left is not None:
                queue.append(current_root.left)
            if current_root.right is not None:
                queue.append(current_root.right)

        return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        if (p is not None and q is None) or (p is None and q is not None):
                return False

        if p.val != q.val:
            return False

        left_subtree = self.isSameTree(p.left, q.left)
        right_subtree = self.isSameTree(p.right, q.right)

        if left_subtree is True and right_subtree is True:
            return True
        else:
            return False