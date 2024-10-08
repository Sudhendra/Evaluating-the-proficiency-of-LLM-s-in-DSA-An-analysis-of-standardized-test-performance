from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []

        def neighbors(word):
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i + 1:]
                    if new_word in wordList and new_word != word:
                        yield new_word
        
        def build_paths(curr, path, paths):
            if curr == beginWord:
                paths.append(path.copy())
                return
            for prev in graph[curr]:
                path.append(prev)
                build_paths(prev, path, paths)
                path.pop()
        
        graph = {word: set() for word in wordList}
        q = [beginWord]
        while q:
            new_q = []
            for word in q:
                wordList.discard(word)
            for word in q:
                for nei in neighbors(word):
                    graph[nei].add(word)
                    if nei in wordList:
                        new_q.append(nei)
            if new_q:
                break
            q = new_q

        paths = []
        build_paths(endWord, [endWord], paths)
        return paths

