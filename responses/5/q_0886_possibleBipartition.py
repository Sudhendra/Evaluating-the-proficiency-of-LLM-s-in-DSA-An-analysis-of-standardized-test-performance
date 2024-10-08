from collections import defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for dislike in dislikes:
            adj_list[dislike[0]].append(dislike[1])
            adj_list[dislike[1]].append(dislike[0])

        colors = [0] * (n + 1)

        def dfs(person, color):
            if colors[person] != 0:
                return colors[person] == color
            colors[person] = color
            for neighbor in adj_list[person]:
                if not dfs(neighbor, -color):
                    return False
            return True

        for person in range(1, n + 1):
            if colors[person] == 0 and not dfs(person, 1):
                return False
        return True
