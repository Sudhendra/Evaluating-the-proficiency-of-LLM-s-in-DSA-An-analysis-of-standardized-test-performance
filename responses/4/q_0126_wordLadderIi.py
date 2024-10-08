from collections import defaultdict, deque

class Solution:
    def findLadders(
        self, beginWord, endWord, wordList
    ):
        wordList = set(wordList)
        if endWord not in wordList:
            return []

        # Build a graph where each word is linked to its neighbors that are one letter different
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                graph[pattern].append(word)

        # Breadth First Search
        queue = deque([(beginWord, [beginWord])])
        found = False
        result = []
        visited = set()

        while queue:
            level = len(queue)
            localVisited = set()

            for _ in range(level):
                currentWord, path = queue.popleft()

                if currentWord == endWord:
                    found = True
                    result.append(path)

                for i in range(len(currentWord)):
                    pattern = currentWord[:i] + '*' + currentWord[i + 1:]

                    for neighbor in graph[pattern]:
                        if neighbor not in visited:
                            queue.append((neighbor, path + [neighbor]))
                            localVisited.add(neighbor)

            visited.update(localVisited)

            if found:
                break

        return result
