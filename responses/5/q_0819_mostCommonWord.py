from typing import List
import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_words = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        word_count = Counter(word for word in words if word not in banned_words)
        return word_count.most_common(1)[0][0]
