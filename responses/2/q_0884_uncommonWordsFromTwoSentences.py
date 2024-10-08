class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_freq = collections.defaultdict(int)
        uncommon_words = []

        for word in s1.split():
            word_freq[word] += 1
        for word in s2.split():
            word_freq[word] += 1

        for word, freq in word_freq.items():
            if freq == 1:
                uncommon_words.append(word)

        return uncommon_words