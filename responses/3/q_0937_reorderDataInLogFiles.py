from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def custom_sort(log):
            identifier, content = log.split(" ", 1)
            return (0, content, identifier) if content[0].isalpha() else (1,)

        return sorted(logs, key=custom_sort)
