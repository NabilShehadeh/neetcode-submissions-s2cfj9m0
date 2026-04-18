# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: # in the case they're both null
            return True # since they would have the same structures. 
        if p and q and p.val == q.val:
            return (self.isSameTree(p.right, q.right) and
            self.isSameTree(p.left, q.left))
        return False # need an and because they have to be the same tree
        