from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]) -> bool:
        visited = set()
        queue = deque([0])
        visited.add(0)

        while queue:
            current_room = queue.popleft()
            for key in rooms[current_room]:
                if key not in visited:
                    queue.append(key)
                    visited.add(key)

        return len(visited) == len(rooms)
