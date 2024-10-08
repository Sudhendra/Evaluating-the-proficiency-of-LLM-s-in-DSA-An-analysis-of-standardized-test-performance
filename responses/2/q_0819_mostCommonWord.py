from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())
        words = [word for word in words if word not in banned]
        word_counts = Counter(words)
        return max(word_counts, key=word_counts.get)
