from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        deadends = set(deadends)
        visited = set()
        queue = [("0000", 0)]

        while queue:
            current, moves = queue.pop(0)
            if current == target:
                return moves
            if current in deadends or current in visited:
                continue

            visited.add(current)

            for i in range(4):
                digit = int(current[i])
                for diff in [1, -1]:
                    new_digit = (digit + diff) % 10
                    new_lock_state = current[:i] + str(new_digit) + current[i + 1:]
                    if new_lock_state not in visited and new_lock_state not in deadends:
                        queue.append((new_lock_state, moves + 1))

        return -1
