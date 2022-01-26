from queue import Queue

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        # words is sorted lexicographically
        # return string of unique letters sorted lex
        # no solution return "", return any solution (aka first solution found)
        # lex sorted = s < t if s[i] < s[t]
        
        """
        ['foo', 'fie', 'fief', 'bar']
        
        f-b, o-i
        
        
        """
        
        if not words:
            return ""

        # put all the unique letters into a set
        # time.O(n*m) space.O(n*m) where n is words and m is characters per word
        unique_letters: Set = set()
        for word in words:
            for letter in word:
                if not letter in unique_letters:
                    unique_letters.add(letter)
        # print(f'unique_letters {unique_letters}')
                    
        # known ordering rules
        # time.O(1) space.O(v) where v is net connectivity of the alien dict
        rules: Dict[str, List[str]] = {}
            
        def is_valid(letter_1: str, letter_2: str) -> bool:
            """ DFS through rules. """
            to_visit: Queue = Queue()
            visited: Set = set()
            if not letter_2 in rules:
                return True
            for letter in rules[letter_2]:
                to_visit.put(letter)
            while not to_visit.empty():
                letter = to_visit.get()
                if letter == letter_1:
                    return False
                visited.add(letter)
                if letter in rules:
                    for _letter in rules[letter]:
                        if not _letter in visited:
                            to_visit.put(_letter)
                            visited.add(_letter)
            return True
            
        # put all the rules into a set
        # time.O(m * n) space.O(1) where n is words and m is characters per word
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j == len(words[i + 1]):
                    return ""
                if not words[i][j] == words[i + 1][j]:
                    if not words[i][j] in rules:
                        rules[words[i][j]] = [words[i + 1][j]]
                    else:
                        rules[words[i][j]].append(words[i + 1][j])
                    if not is_valid(words[i][j], words[i + 1][j]):
                        return ""
                    break
        # print(f'rules {rules}')
                    
        # graph of connections, topological sort
        # time.O(v) space.O(b) where b is unique characters in alien dict
        in_edges: Dict[str, int] = {}
        for letter, letters in rules.items():
            in_edges[letter] = in_edges.get(letter, 0)
            for _letter in letters:
                in_edges[_letter] = in_edges.get(_letter, 0) + 1
        # print(f'in_edges {in_edges}')
        
        # string of letters in lexico order
        # time.O(1) space.O(b) where b is unique characters in alien dict
        result: str = ''
        
        # letters with no incoming edges
        # time.O(1) space.O(b) where b is unique characters in alien dict
        topo: Queue() = Queue()
        for letter, edge_count in in_edges.items():
            if edge_count == 0:
                topo.put(letter)
        while not topo.empty():
            letter = topo.get()
            result += letter
            unique_letters.remove(letter)
            del in_edges[letter]
            for _letter, letters in rules.items():
                if _letter == letter:
                    for __letter in letters:
                        in_edges[__letter] -= 1
                        if in_edges[__letter] == 0:
                            topo.put(__letter)
            
        return result + ''.join(unique_letters)
