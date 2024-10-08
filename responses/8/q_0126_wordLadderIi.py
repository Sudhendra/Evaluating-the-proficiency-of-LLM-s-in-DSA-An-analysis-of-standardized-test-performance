from collections import defaultdict, deque

class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        if endWord not in wordList:
            return []

        wordList = set(wordList)
        graph = defaultdict(list)
        level = {beginWord: [[beginWord]]}

        def is_adjacent(word1, word2):
            diff = 0
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1

        while level:
            new_level = defaultdict(list)
            for word in level:
                if word == endWord:
                    return level[word]
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in wordList and is_adjacent(word, new_word):
                            for path in level[word]:
                                new_level[new_word].append(path + [new_word])
            wordList -= set(new_level.keys())
            level = new_level

        return []
