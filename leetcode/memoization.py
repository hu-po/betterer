#     @functools.cache
#     def fib(self, n: int) -> int:
        
#         # Time O(N)
#         # Space O(N)
        
#         if n < 2:
#             return n
#         return self.fib(n-2) + self.fib(n-1)
    
    def fib(self, n:int) -> int:
        
        # Time O(N)
        # Space O(N)
        
        cache: typing.Dict = {0:0, 1:1}
        for i in range(2, n+1):
            cache[i] = cache[i-2] + cache[i-1]
            
        return cache[n]

   def climbStairs(self, n: int) -> int:
    
        cache: Dict = {}
        
        def climb(n: int) -> int:
            if cache.get(n, None) is not None:
                return cache[n]
            if n < 2:
                return 1
            cache[n] = climb(n-1) + climb(n-2)
            return cache[n]
        
        return climb(n)
