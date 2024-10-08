from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)
        sentence_list = sentence.split()
        result = []
        for word in sentence_list:
            prefix = ''
            for i in range(1, len(word)):
                if word[:i] in roots:
                    prefix = word[:i]
                    break
            result.append(prefix if prefix else word)
        return ' '.join(result)
