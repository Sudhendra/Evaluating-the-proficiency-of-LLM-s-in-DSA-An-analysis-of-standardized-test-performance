from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))  # Sort people by descending height and ascending number of taller people in front
        result = []
        for p in people:
            result.insert(p[1], p)  # Insert the person at index p[1] to reconstruct the queue
        return result
