from collections import Trie

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=lambda x: x[::-1])
        trie = Trie()
        count = 0
        for word in words:
            if trie.add(word[::-1]):
                count += len(word) + 1
        return count
