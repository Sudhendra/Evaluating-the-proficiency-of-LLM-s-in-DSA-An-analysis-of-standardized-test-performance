from collections import Counter
import re
from typing import List

class Solution:

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())
        word_count = Counter(word for word in words if word not in banned)
        return word_count.most_common(1)[0][0]
