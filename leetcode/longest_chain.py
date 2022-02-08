from typing import List, Dict, Set
from queue import Queue

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        # word: List[str] - lowercase english letters
        # predecessor b of a if a single char can be inserted in a to create b
        # word chain of len k >= 1, words are predecessors of each other
        # return the length of longest possible word chain
        
        # check inputs, edge cases
        
        # words list is empty
        if not words:
            return 0
        
        # words list is len 1
        if len(words) == 1:
            return 1
        
        # is everthing a string? what about empty characters?
        
        # predecessors must be of lesser length than next word
        
        # is words sorted based on length of words?
        
        # time O(NlogN + N*(N) + N) ~ O(N**2) where N is length of words list
        # space O(1 + N + 1) ~ O(N)
        
        words = sorted(words, key=lambda word: len(word))
    
        # is this a graph problem? building a graph and then finding longest path from root-leaf?
        
        # can we do this in place?
        # could we keep track of what chains are running as we move through the words list?
        # in that siutation you would use memory and this would be similar to graph approach
        
        # how to determine if succesive words are predecessors?
        # create sets and check for equality
        # length needs to be n-1
        
        # could this be easier to do backwards?
        
        @functools.lru_cache
        def is_predecessor(a: str, b: str) -> bool:
            """ Is word A a predecessor to word b. """
            if not len(a) == len(b) - 1:
                return False
            pa: int = 0
            pb: int = 0
            one_difference_found: bool = False
            while pa < len(a):
                if not a[pa] == b[pb]:
                    if not one_difference_found:
                        one_difference_found = True
                        pb += 1
                    else:
                        return False
                pa += 1
                pb += 1
            return True
            
        
        """
        ['a', 'b', 'ab', 'ac', 'abc']
        ['abc', 'ac', 'ab', 'b', 'a']
        chains={'abc':1, 'ac':1, 'ab':1, 'b':1, 'a':1}
        i=0,word='abc'
            _word='ac', chains={'abc':1, 'ac':2, 'ab':1, 'b':1, 'a':1}
            _word='ab', chains={'abc':1, 'ac':2, 'ab':2, 'b':1, 'a':1}
            _word='b'
        i=1,word='ac'
            _word='ab'
            _word='b'
            _word='a', chains={'abc':1, 'ac':2, 'ab':2, 'b':1, 'a':3}
        """
        
        chains: Dict[str, int] = {word : 1 for word in words}

        for i, word in enumerate(words):
            if i + 1 == len(words):
                break
            for _word in words[i+1:]:
                if len(_word) > len(word) + 1:
                    break
                if len(_word) == len(word):
                    continue
                if is_predecessor(word, _word):
                    chains[_word] = max(chains[_word], chains[word] + 1)
               
        max_chain_len: int = 1
        for word, chain_len in chains.items():
            if chain_len > max_chain_len:
                max_chain_len = chain_len
        return max_chain_len
        
