    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # Time O(N)
        # Space O(N)
        
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
    def myPow(self, x: float, n: int) -> float:
        
        # Time O(N)
        # Space O(1)
        
        if n == 0:
            return 1
        solution: int = x
        neg: bool = (n < 0)
        n = abs(n)
        while n > 1:
            solution *= x
            n -= 1
        if neg:
            return 1/ solution
        return solution
