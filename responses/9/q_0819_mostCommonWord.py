from typing import List
import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word.lower() for word in re.findall(r'\w+', paragraph) if word.lower() not in banned]
        word_counts = Counter(words)
        return max(word_counts, key=word_counts.get)
