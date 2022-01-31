class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        # time O(N*N)
        # space O(N*N)


        def _valid_sentences(s: str) -> List[str]:

            # base case
            if not s:
                return []

            answer: List[str] = []

            # fast lookup through dict
            curr: int = 1
            while curr < len(s)+1:
                if curr == len(s) and s[:curr] in wordDict:
                    answer.append(s[:curr])
                if s[:curr] in wordDict:
                    for sentence in _valid_sentences(s[curr:]):
                        answer.append(f"{s[:curr]} {sentence}")
                curr += 1
            
            return answer

        return _valid_sentences(s)
