from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())
        words = [w for w in words if w not in banned]
        count = Counter(words)
        return max(count, key=count.get)
