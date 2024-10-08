class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = collections.Counter(words)
        sorted_words = sorted(word_count, key=lambda x: (-word_count[x], x))
        return sorted_words[:k]