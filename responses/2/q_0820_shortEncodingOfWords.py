class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words_set = set(words)
        for word in words:
            for i in range(1, len(word)):
                words_set.discard(word[i:])
        return sum(len(word) + 1 for word in words_set)

# Another possible solution
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = sorted(word[::-1] for word in words)
        res = 0
        prev = ""
        for word in words:
            if not prev.endswith(word):
                res += len(word) + 1
            prev = word
        return res
