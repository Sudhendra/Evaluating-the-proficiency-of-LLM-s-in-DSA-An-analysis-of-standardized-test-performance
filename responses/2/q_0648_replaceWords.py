class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root_set = set(dictionary)
        words = sentence.split()
        result = []
        
        for word in words:
            prefix = ''
            for i in range(1, len(word) + 1):
                if word[:i] in root_set:
                    prefix = word[:i]
                    break
            result.append(prefix if prefix else word)
        
        return ' '.join(result)