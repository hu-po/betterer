from typing import List
from queue import PriorityQueue

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        # space O(C) ~ O(1)
        # time O(N*(N)) ~ O(N*N)
        
        # edge cases
        if not answerKey:
            return 0
        # k == 0, can't modify answerKey
        
        max_c: int = 0
        lo: int = 0
        hi: int = 0
        c_t: int = 0
        c_f: int = 0
            
        for hi in range(len(answerKey)):
            if answerKey[hi] == 'T':
                c_t += 1
            elif answerKey[hi] == 'F':
                c_f += 1
            else:
                raise ValueError(f'answerKey contains non T or F value at index {hi}')
        
            while c_t > k and c_f > k:
                if answerKey[lo] == 'T':
                    c_t -= 1
                elif answerKey[lo] == 'F':
                    c_f -= 1   
                lo += 1
            
            max_c = max((hi - lo + 1), max_c)
                
        return max_c
    
# # [TTFTFTTFF], k = 2

# lo = 0, hi = 0, ct = 1, cf = 0, k=2
#     max_c = 1
# lo = 0, hi = 1, ct = 2, cf=0, k=2
#     max_c = 2
# lo = 0, hi = 2, ct = 2, cf=1, k=2
#     max_c = 3
# lo = 0, hi = 3, ct = 3, cf=1, k=2
#     max_c = 4
# lo = 0, hi = 4, ct = 3, cf=1, k=2
    

# lo = 0, char = T, c_t = 1, c_f = 0, hi = 1
#     answerKey[hi] = T, c_t = 2, c_f = 0, hi = 2, max_c=2
#     answerKey[hi] = F, c_t = 2, c_f = 1, hi = 3, max_c=3
#     answerKey[hi] = T, c_t = 3, c_f = 2, hi = 3, max_c=3

        
        # algo
        # go through answerKey and count the number of consecutive Ts or Fs
        # Two separate lists (one for T, one for F)
        # max consecutive = we will only ever use all our Ks for either Ts or Fs
        
#         ts: List = [0] * len(answerKey)
#         fs: List = [0] * len(answerKey)
        
#         max_cc: int = 0
#         cc_t: int = 0
#         cc_f: int = 0
            
#         start_i: int = 0
#         end_i: int = 0
        
#         # (priority, (T or F, start_i, end_i))
#         cc_q: PriorityQueue = PriorityQueue()
            
#         for i, char in answerKey:
            
#             if char == 'T':
                
#                 if cc_f > 0:
#                     cc_q.put((-ccf, ('F', start_i, end_i)))
#                     cc_f = 0
                    
#                 if cc_t == 0:
#                     start_i = i
#                     end_i = i
#                 else:
#                     end_i = i
#                 cc_t += 1
#                 ts[i] = cc_t
                
#             elif char == 'F':
                
#                 if cc_t > 0:
#                     cc_q.put((-cct, ('T', start_i, end_i)))
#                     cc_t = 0
#                 if cc_f == 0:
#                     start_i = i
#                     end_i = i
#                 else:
#                     end_i = i
#                 cc_f += 1
#                 fs[i] = cc_f
                    
#             if cc_t > max_cc or cc_f > max_cc:
#                 max_cc = max(cc_t, cc_f)
        
#         # return
#         return max_cc

    
# [TTFTF], k=1

# cc_q = (
#     (-2, (T, 0, 2)),
#     (-1, (F, 2, 3)),
#     (-1, (T, 3, 4)),
#     (-1, (F, 4, 2)),
# )
# ts = [12010]
# fs = [00101]
        
