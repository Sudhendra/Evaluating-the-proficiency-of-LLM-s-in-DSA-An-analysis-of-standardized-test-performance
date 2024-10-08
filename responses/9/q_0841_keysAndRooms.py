from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        visited[0] = True
        
        stack = [0]
        
        while stack:
            current_room = stack.pop()
            for key in rooms[current_room]:
                if not visited[key]:
                    visited[key] = True
                    stack.append(key)
        
        return all(visited)
