class Solution:
    def isSameTree(self, p, q):
        # Case 1: both are None
        if not p and not q:
            return True
        
        # Case 2: one is None or values differ
        if not p or not q or p.val != q.val:
            return False
        
        # Case 3: check left and right recursively
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))