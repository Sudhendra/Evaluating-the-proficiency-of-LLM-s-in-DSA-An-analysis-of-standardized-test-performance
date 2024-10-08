from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]) -> bool:
        n = len(rooms)
        visited = set()
        stack = [0]

        while stack:
            current_room = stack.pop()
            visited.add(current_room)

            for key in rooms[current_room]:
                if key not in visited:
                    stack.append(key)

        return len(visited) == n