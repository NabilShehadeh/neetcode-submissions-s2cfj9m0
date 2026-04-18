# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        if not s:
            return False
        if self.SameTree(s,t):
            return True
        return (self.isSubtree(s.left, t) or # here we're checking to find the subtree somewhere
        self.isSubtree(s.right, t)) # is the tree in the left or the right subtree
    
    def SameTree(self, s, t):
        if not s and not t:
            return True # since we're using the same tree here and looking for it 
            # we need to use ands to ensure they're the exact same to be a same tree.
        if s and t and s.val == t.val:
            return (self.SameTree(s.left, t.left) and # here we verify a complete match
            self.SameTree(s.right, t.right))
        return False
        