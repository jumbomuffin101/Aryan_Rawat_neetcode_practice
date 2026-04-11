# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot == None:
            return True
        
        def isSameTree(a, b):
            if a == None and b == None:
                return True
            if a == None or b == None:
                return False
            if a.val != b.val:
                return False
            left = isSameTree(a.left, b.left)
            right = isSameTree(a.right, b.right)

            return left and right

        if root == None:
            return False

        if isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
