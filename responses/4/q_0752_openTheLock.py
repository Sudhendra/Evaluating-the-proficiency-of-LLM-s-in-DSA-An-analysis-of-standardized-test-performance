from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1

        queue = [("0000", 0)]
        visited = set("0000")

        while queue:
            current, turns = queue.pop(0)

            if current == target:
                return turns

            for i in range(4):
                for move in [-1, 1]:
                    new_num = current[:i] + str((int(current[i]) + move) % 10) + current[i+1:]

                    if new_num not in dead and new_num not in visited:
                        queue.append((new_num, turns + 1))
                        visited.add(new_num)

        return -1
