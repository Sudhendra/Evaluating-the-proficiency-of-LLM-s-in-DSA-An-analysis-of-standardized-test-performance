from collections import defaultdict, deque

class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        
        wordList = set(wordList)
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                wildCard = word[:i] + '*' + word[i+1:]
                graph[wildCard].append(word)
        
        res = []
        visited = set([beginWord])
        q = deque([(beginWord, [beginWord])])
        found = False
        
        while q and not found:
            level = set()
            for _ in range(len(q)):
                curr, path = q.popleft()
                for i in range(len(curr)):
                    wildCard = curr[:i] + '*' + curr[i+1:]
                    for next_word in graph[wildCard]:
                        if next_word == endWord:
                            found = True
                            res.append(path + [endWord])
                        if next_word not in visited:
                            level.add(next_word)
                            q.append((next_word, path + [next_word]))
            visited = visited.union(level)
        
        return res
