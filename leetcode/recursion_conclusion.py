    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Time O(N + M) ~ O(N)
        # Space O((N + M) + 1) ~ O(N)
        
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        
        sol: ListNode = ListNode()
        solhead: ListNode = sol
            
        while list1 or list2:
            if not list1:
                sol.next = list2
                list2 = list2.next
            elif not list2:
                sol.next = list1
                list1 = list1.next
            elif list1.val <= list2.val:
                sol.next = list1
                list1 = list1.next
            elif list1.val >= list2.val:
                sol.next = list2
                list2 = list2.next
            sol = sol.next
            
        return solhead.next
      
    def kthGrammar(self, n: int, k: int) -> int:
        """
0
01
0110
01101001

len(s) = 2^n

n - 1, 

n=4,k=3 -> n=3,k=2
n=4,k=4 -> opposite of n=3,k=2
n=3,k=3 -> n=2,k=2
n=3,k=4 -> opposite of n=2,k=2
        """
        
        # Time O(N)
        # Space O(N)
        
        # base case
        if n == 1:
            return 0
        elif n == 2:
            if k == 1:
                return 0
            if k == 2:
                return 1
        else:
            if k % 2 == 0:
                return int(not self.kthGrammar(n-1, k // 2))
            else:
                return self.kthGrammar(n-1, (k // 2) + 1)

        # prevrow: str = '0'
        # for _ in range(0, n):
        #     row: str = ''
        #     for char in prevrow:
        #         if char == '0':
        #             row += '01'
        #         elif char == '1':
        #             row += '10'
        #     prevrow = row
        # return int(row[k-1])

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """
        each node can have 2 subnodes, 1 subnode, or no subnodes
        can we have cycles? (1 -> 3 -> 2) No: these are search trees
        depth of tree can at most be n, at least be 1, 3, 7, 
        recursive, pick root node, all sub-trees plus that
        symmetric trees? 1 -> 23 same as 1 -> 32
        search trees, so left < right
        
        leaf nodes are always double null
        1-branch nodes doesn't matter left and right
        2-branch nodes doesn't matter left and right
        
        budget of n-2 branches
        """

        if n == 1:
            return [TreeNode(1)]
        
        def make_trees(first: int, last: int) -> List[Optional[TreeNode]]:
            trees: List[Optional[TreeNode]] = []
            for root in range(first, last+1):
                for left in make_trees(first, root-1):
                    for right in make_trees(root+1, last):
                        trees += [TreeNode(val=root, left=left, right=right)]
            return trees or [None]
        
        return make_trees(1, n)
