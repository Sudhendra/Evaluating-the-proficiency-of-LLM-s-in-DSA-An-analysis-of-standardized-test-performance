from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        deadends = set(deadends)
        queue = [("0000", 0)]
        visited = set("0000")

        while queue:
            current, turns = queue.pop(0)

            if current == target:
                return turns

            if current in deadends:
                continue
            
            for i in range(4):
                for move in [-1, 1]:
                    new_digit = str((int(current[i]) + move) % 10)
                    new_combination = current[:i] + new_digit + current[i+1:]

                    if new_combination not in visited:
                        visited.add(new_combination)
                        queue.append((new_combination, turns + 1))

        return -1
