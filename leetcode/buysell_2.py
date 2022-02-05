class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # price of stock on day i
        # choose day to buy and choose day to sell
        # return max profit
        
        # check inputs, edge cases
        if not prices or len(prices) <= 1:
            return 0
        
        
        # time O(N) where N is length of prices list
        # space O(1)
        
        max_profit: int = 0
        min_price: int = float('inf')
            
        # cumulative score on prices
        for price in prices:        
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
           
        """
        [1 2 7 1 6]
        [0 1 5 -6 5]
        [0 1 6 -1 4]
        
        buy at min, sell at max
        min = -2, max = 8
        
        
        """
        
        return max_profit
        
