from typing import List

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        occurrences = []
        for i in range(2, len(words)):
            if words[i - 2] == first and words[i - 1] == second:
                occurrences.append(words[i])
        return occurrences
