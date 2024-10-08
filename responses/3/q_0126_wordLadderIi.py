from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []

        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                graph[pattern].append(word)

        queue = deque([(beginWord, [beginWord])])
        visited = set([beginWord])
        found = False
        result = []

        while queue and not found:
            level_visited = set()
            for _ in range(len(queue)):
                current_word, path = queue.popleft()
                
                for i in range(len(current_word)):
                    pattern = current_word[:i] + '*' + current_word[i+1:]
                    for neighbor in graph[pattern]:
                        if neighbor == endWord:
                            result.append(path + [endWord])
                            found = True
                        if neighbor not in visited:
                            queue.append((neighbor, path + [neighbor]))
                            level_visited.add(neighbor)
            visited.update(level_visited)

        return result
