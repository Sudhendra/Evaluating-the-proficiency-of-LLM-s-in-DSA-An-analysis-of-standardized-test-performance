class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re
        from collections import Counter
        
        words = [word.lower() for word in re.findall(r'\w+', paragraph) if word.lower() not in banned]
        
        word_count = Counter(words)
        
        return word_count.most_common(1)[0][0]