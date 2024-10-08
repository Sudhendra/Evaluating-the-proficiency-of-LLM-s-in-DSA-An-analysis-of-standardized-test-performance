from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)
        
        def replace_word(word):
            for i in range(1, len(word)):
                if word[:i] in roots:
                    return word[:i]
            return word
        
        return ' '.join(replace_word(word) for word in sentence.split())

# Solution to be implemented in replaceWords method
