from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)
        sentence = sentence.split()
        
        for i in range(len(sentence)):
            for root in roots:
                if sentence[i].startswith(root):
                    sentence[i] = root
                    break
        
        return ' '.join(sentence)
