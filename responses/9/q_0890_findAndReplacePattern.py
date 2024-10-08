from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word, pattern):
            if len(word) != len(pattern):
                return False
            
            word_to_pattern = {}
            pattern_to_word = {}
            for i in range(len(word)):
                if word[i] not in word_to_pattern:
                    word_to_pattern[word[i]] = pattern[i]
                if pattern[i] not in pattern_to_word:
                    pattern_to_word[pattern[i]] = word[i]
                if word_to_pattern[word[i]] != pattern[i] or pattern_to_word[pattern[i]] != word[i]:
                    return False
                
            return True
        
        result = []
        for word in words:
            if match(word, pattern):
                result.append(word)
        
        return result
