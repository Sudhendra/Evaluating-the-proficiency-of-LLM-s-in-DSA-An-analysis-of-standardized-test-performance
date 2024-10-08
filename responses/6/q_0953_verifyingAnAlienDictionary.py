class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {char: index for index, char in enumerate(order)}

        def is_sorted(word1, word2):
            n, m = len(word1), len(word2)
            for i in range(min(n, m)):
                if word1[i] != word2[i]:
                    return order_dict[word1[i]] <= order_dict[word2[i]]
            return n <= m

        for i in range(1, len(words)):
            if not is_sorted(words[i - 1], words[i]):
                return False
        return True
