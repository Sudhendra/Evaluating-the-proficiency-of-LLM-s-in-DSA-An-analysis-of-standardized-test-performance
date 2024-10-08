from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        word_set, longest_word = set(), ""
        
        for word in words:
            if len(word) == 1 or word[:-1] in word_set:
                word_set.add(word)
                if len(word) > len(longest_word):
                    longest_word = word
                
        return longest_word
