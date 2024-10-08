class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]) -> bool:
        visited = set([0])
        stack = [0]

        while stack:
            current_room = stack.pop()
            for key in rooms[current_room]:
                if key not in visited:
                    visited.add(key)
                    stack.append(key)

        return len(visited) == len(rooms)