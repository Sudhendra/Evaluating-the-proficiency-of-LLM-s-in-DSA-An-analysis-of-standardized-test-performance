from collections import defaultdict
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []

        neighbors = defaultdict(list)
        word_len = len(beginWord)
        for word in wordList:
            for i in range(word_len):
                key = word[:i] + '*' + word[i + 1:]
                neighbors[key].append(word)

        def bfs():
            queue = [(beginWord, [beginWord])]
            visited = set()
            found = False
            while queue and not found:
                next_level = set()
                for word, path in queue:
                    visited.add(word)
                    for i in range(word_len):
                        key = word[:i] + '*' + word[i + 1:]
                        for neighbor in neighbors[key]:
                            if neighbor not in visited:
                                if neighbor == endWord:
                                    found = True
                                    yield path + [neighbor]
                                next_level.add((neighbor, path + [neighbor]))
                if not found:
                    queue = next_level

        return list(bfs())
