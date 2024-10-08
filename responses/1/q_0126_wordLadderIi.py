from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []

        word_len = len(beginWord)
        frontiers = {beginWord: [[beginWord]]}
        while frontiers:
            new_frontiers = {}
            wordList -= set(frontiers.keys())
            for word, paths in frontiers.items():
                if word == endWord:
                    return paths
                for i in range(word_len):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + char + word[i + 1:]
                        if new_word in wordList:
                            if new_word not in new_frontiers:
                                new_frontiers[new_word] = [path + [new_word] for path in paths]
                            else:
                                new_frontiers[new_word] += [path + [new_word] for path in paths]
            frontiers = new_frontiers
        
        return []