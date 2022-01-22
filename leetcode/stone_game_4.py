from typing import Set

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        # 2 player game, Alice starts Bob next and then alternate
        # n stones in a pile
        # 1 move per turn
        # move is remove a non-zero square number of stones
        # if player cannot make move they lose
        
        # return true if alice wins, both players play optimally
        
        # since both players play optimally, assume a single player is playing
        # and the question is now whether it ends on an even or an odd turn
        
        # total_turn: int = 0
            
        # Alice, Bob, Alice (alice wins in turn 2, return True)
        
        # squares are 1, 4, 9, etc
        # in each turn a player can only remove up until x**2 <= stones_left
        # we can use n directly as stones left (in place)
        
#         while n > 0:
            
#             # if the number of stones left is a square, then take that number of stones
#             if int(math.sqrt(n)) ** 2 == n:
#                 n -= n
#             else:
#                 # take number of stones required to result in a non-square number of stones?
                
#                 # what are the possible turns?
#                 possible_turns: Set = set()
#                 for turn in (i**2 for i in range(1, n)):
#                     if turn < n:
#                         possible_turns.add(turn)
#                     else:
#                         break
                        
#                 # if only one possible turn, take it
#                 if len(possible_turns) <= 1:
#                     n -= possible_turn.pop()
#                     break
                        
#                 # Remove the turns where n - possible_turn is a square
#                 better_turns: Set = set()
#                 for turn in possible_turns:
#                     if not ((n - turn) in possible_turns):
#                         better_turns.add(turn)
                        
                
#                 # if only one possible turn, take it
#                 if len(better_turns) <= 1:
#                     n -= better_turns.pop()
#                     break
                
#             # increment turn variable
#             total_turn += 1
            
        
#         if total_turn % 2 == 0:
#             return True
#         return False

        # Looked at solution, its a memoized DFS, implementation:
    
        @functools.cache
        def dfs(n: int) -> bool:
            ''' Can a player win at this state? '''
            if n <= 1:
                return bool(n)
            for to_take in (i**2 for i in range(1, n)):
                if to_take > n:
                    break
                if not dfs(n - to_take):
                    return True
            return False
        
        return dfs(n)
            
            
        
