class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        # s1: str
        # s2: str
        # s1 and s2 are same length
        # string swap - choose two indices and swap characters
        # return boolean if possible to make both strings equal by performing
        # a string swap on one of the strings

        """
        s1='bank',s2='kanb' > true
        s1='',s2='' > true
        s1='',s2='asdf' > false
        s1='asdf',s2='' > false
        s1='ab',s2='a' > false
        s1='ab',s2='abc' > false

        s1='abcot',s2='cabto' > false
        s1=['a','b','c']
        s2=['c', 'b','a']
        p1=0
            s1=['c','b','a', 'o', 't']        
                return false

        """

        # check inputs and edge cases

        # # make sure all lowercase
        # s1 = s1.lowercase()
        # s2 = s2.lowercase()

        if s1 == s2:
            return True

        if not s1 or not s2:
            return False

        if not len(s1) == len(s2):
            return False

        if not set(s1) == set(s2):
            return False

        # Convert to lists
        s1: List[str] = list(s1)
        s2: List[str] = list(s2)
            
        # remove any common letters
        i: int = 0
        while i < len(s1):
            if s1[i] == s2[i]:
                del s1[i]
                del s2[i]
            else:
                i += 1

        i: int = 0
        while i < len(s1):
            if not s1[i] == s2[i]:
                # the letter you wish was there, is it in the remaining part of the word?
                if s2[i] in s1[i+1:]:
                    # yes it is, swap the letters and check for equality
                    idx: int = s1[i+1:].index(s2[i]) + i + 1
                    # print(f"idx={idx}")
                    s1[i], s1[idx] = s1[idx], s1[i]
                    # at most have one swap, so check for equality
                    # print(f"s1={''.join(s1)}")
                    # print(f"s2={''.join(s2)}")
                    if s1 == s2:
                        return True
                    else:
                        return False
                else:
                    return False
            i += 1

        # time O(1 + 1 + 1 + 1 + 1 + N*(1 + 1 + 1)) ~ O(N)
        # space O(1) ~ O(1)

        return True
