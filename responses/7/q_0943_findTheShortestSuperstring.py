from itertools import permutations

class Solution:
    def combine_strings(self, str1, str2):
        for i in range(len(str1)):
            if str2.startswith(str1[i:]):
                return str1[:i] + str2
        return str1 + str2

    def shortestSuperstring(self, words: List[str]) -> str:
        words = set(words)
        while len(words) > 1:
            max_overlap = float('-inf')
            pair = ()
            for pair_words in permutations(words, 2):
                overlap = len(self.combine_strings(*pair_words)) - len(pair_words[0])
                if overlap > max_overlap:
                    max_overlap = overlap
                    pair = pair_words

            words.remove(pair[0])
            words.remove(pair[1])
            words.add(self.combine_strings(*pair))
        
        return words.pop()
