from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)
        replaced = []

        for word in sentence.split():
            found_root = None
            for i in range(1, len(word)):
                if word[:i] in roots:
                    found_root = word[:i]
                    break

            replaced.append(found_root if found_root else word)

        return ' '.join(replaced)
