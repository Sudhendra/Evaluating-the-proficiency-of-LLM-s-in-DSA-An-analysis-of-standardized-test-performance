from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]) -> bool:
        n = len(rooms)
        visited = set()
        visited.add(0)
        queue = deque([0])

        while queue:
            curr_room = queue.popleft()
            for key in rooms[curr_room]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)

        return len(visited) == n
