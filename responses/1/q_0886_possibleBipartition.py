class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for dislike in dislikes:
            graph[dislike[0]].append(dislike[1])
            graph[dislike[1]].append(dislike[0])

        colors = [0] * (n + 1)

        def dfs(person, color):
            if colors[person] != 0:
                return colors[person] == color
            colors[person] = color
            for other in graph[person]:
                if not dfs(other, -color):
                    return False
            return True

        for i in range(1, n + 1):
            if colors[i] == 0 and not dfs(i, 1):
                return False
        return True
