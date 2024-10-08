from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def sort_logs(log):
            identifier, content = log.split(" ", 1)
            return (0, content, identifier) if content[0].isalpha() else (1, )

        return sorted(logs, key=sort_logs)
