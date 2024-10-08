class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)
        words = sentence.split()
        new_sentence = []

        for word in words:
            prefix = ''
            for i in range(1, len(word)):
                prefix = word[:i]
                if prefix in roots:
                    break
            new_sentence.append(prefix)

        return ' '.join(new_sentence)
