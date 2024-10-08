class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re
        from collections import Counter

        words = re.findall(r'\w+', paragraph.lower())
        words = [word for word in words if word not in banned]

        word_counts = Counter(words)
        most_common_word = word_counts.most_common(1)[0][0]

        return most_common_word