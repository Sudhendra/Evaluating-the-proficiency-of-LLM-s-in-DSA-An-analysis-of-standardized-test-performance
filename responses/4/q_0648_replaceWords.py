from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root_set = set(dictionary)
        words = sentence.split()
        for i in range(len(words)):
            for j in range(1, len(words[i])):
                if words[i][:j] in root_set:
                    words[i] = words[i][:j]
                    break
        return ' '.join(words)
