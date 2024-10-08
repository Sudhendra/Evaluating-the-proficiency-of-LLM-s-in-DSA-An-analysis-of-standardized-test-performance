from collections import defaultdict

class Solution:
    def findAndReplacePattern(self, words, pattern):
        def match(word):
            if len(word) != len(pattern):
                return False
            
            char_map = {}
            used_chars = set()
            
            for i in range(len(word)):
                if pattern[i] not in char_map:
                    if word[i] in used_chars:
                        return False
                    char_map[pattern[i]] = word[i]
                    used_chars.add(word[i])
                elif char_map[pattern[i]] != word[i]:
                    return False
            
            return True
        
        return [word for word in words if match(word)]
