from collections import Counter, defaultdict
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = Counter(words)
        freq_words = defaultdict(list)
        for word, count in word_count.items():
            freq_words[count].append(word)

        heap = []
        for freq, words_list in freq_words.items():
            heapq.heappush(heap, (-freq, sorted(words_list)))

        result = []
        while k > 0:
            freq, words_list = heapq.heappop(heap)
            result.extend(words_list[:min(len(words_list), k)])
            k -= min(len(words_list), k)

        return result