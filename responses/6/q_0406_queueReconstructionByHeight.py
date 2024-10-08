from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))  # Sort people by height descending and then by number of people in front ascending
        queue = []
        for p in people:
            queue.insert(p[1], p)  # Insert person at index k which represents the number of people taller or equal in front
        return queue
