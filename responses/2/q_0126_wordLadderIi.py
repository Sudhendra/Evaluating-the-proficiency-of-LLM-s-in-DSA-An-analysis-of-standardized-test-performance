from typing import List

class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []

        def construct_paths(path, word, paths):
            if word == beginWord:
                paths.append([beginWord] + path)
                return
            for prev_word in graph[word]:
                construct_paths([word] + path, prev_word, paths)

        def bfs(level, targets, is_forwards):
            if len(level[0]) > len(wordList) or not level[0]:
                return
            if len(level[0]) > len(level[1]):
                return bfs(level[1], targets, not is_forwards)

            next_level = [set() for _ in range(2)]
            finished = False
            for word in level[0]:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in graph and next_word not in level[0]:
                            if next_word in level[1]:
                                finished = True
                                targets.add((word, next_word) if is_forwards else (next_word, word))
                            else:
                                next_level[0].add(next_word)
                            if is_forwards:
                                graph[word].add(next_word)
                            else:
                                graph[next_word].add(word)
            return finished or bfs(next_level, targets, is_forwards)

        graph = {word: set() for word in wordList | {beginWord, endWord}}
        bfs([{beginWord}, {endWord}], set(), True)
        paths = []
        construct_paths([], endWord, paths)
        return paths