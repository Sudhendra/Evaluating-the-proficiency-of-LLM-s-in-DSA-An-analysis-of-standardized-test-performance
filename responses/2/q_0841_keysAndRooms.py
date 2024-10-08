from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]) -> bool:
        n = len(rooms)
        visited = set()

        def dfs(room_num):
            visited.add(room_num)
            for key in rooms[room_num]:
                if key not in visited:
                    dfs(key)

        dfs(0)
        return len(visited) == n