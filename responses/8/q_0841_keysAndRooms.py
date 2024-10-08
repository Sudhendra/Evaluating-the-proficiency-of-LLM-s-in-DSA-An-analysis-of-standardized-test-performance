from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]) -> bool:
        n = len(rooms)
        visited = [False] * n
        visited[0] = True
        queue = deque([0])

        while queue:
            current_room = queue.popleft()
            for key in rooms[current_room]:
                if not visited[key]:
                    visited[key] = True
                    queue.append(key)

        return all(visited)
