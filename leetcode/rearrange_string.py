class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        
        # rearrange s such that same characters are distance k from each other
        # if not possible to re-arrange string, return empty
        
        # check inputs, edge cases
        
        if not k:
            return s
        
        if not s:
            return ""
        
        # time O(NlogN)
        # space O(N)
        # - where N is length of string s
        
        s_count: Dict[str, int] = collections.Counter(s)
        s_count: List[Tuple[str, int]] = sorted(s_count.items(), reverse=True, key=lambda item: item[1])
        
#         multis: Dict[str, int] = {}
#         for char, count in s_count.items():
#             if count > 1:
#                 multis[char] = count
        
#         if len(multis) == 0:
#             return s
        
        # all letters are unique
        if s_count[0][1] == 1:
            return s
        
        # not all letters are unique and k is bigger than s
        if k > len(s):
            return ""
        
        # most common letter has too many instances to fit in s
        if (s_count[0][1] - 1)*k > len(s):
            return ""
        
        """
        "aabbc" k=3
        s_count={a:2,b:2,c:1}
        restr='00000'
            j=0, char=a, count=2
            5 - 2 < ((2 - 1) * 3)
                i=0,rest='a0000'
                i=1,rest='a00a0'
            j=1, char=b, count 2
            5 - 2 < ((2 - 1) * 3)
                i=0,_idx=1+0*3,rest='ab0a0'
                i=1,_idx=1+1*3,rest='ab0ab'
            j=2, char=c, count 1
            5 - 1 < ((1 - 1) * 3)
                i=0,_idx=2+0*3,rest='abcab'
        return 'abcab'
        
        
        """
        
        # main algo
        
        # creating the rearranged string
        restr: List[str] = [None] * len(s)
        
        # separate the most numerous character first
        # if there isn't enough characters left to separate the numerous characters, break
        for j, (char, count) in enumerate(s_count):
            # is there even enough characters left?
            if (len(s) - count) < ((count - 1) * k):
                return ""
            for i in range(count):
                if j+i*k > len(s):
                    return ""
                if restr[j + i*k] is None:
                    restr[j + i*k] = char
                else:
                    restr[restr.index(None)] = char
            
        # adding characters to restr one at a time, decreasing the len of s_counter values
        # priority queue
        
        return ''.join(restr)
