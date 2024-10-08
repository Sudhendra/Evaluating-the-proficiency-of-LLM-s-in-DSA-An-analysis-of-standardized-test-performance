from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def custom_sort(log):
            identifier, rest = log.split(" ", 1)
            return (0, rest, identifier) if rest[0].isalpha() else (1,)
        
        return sorted(logs, key=custom_sort)

# Time complexity: O(M*N*log(N)), where M is the average length of each log and N is the number of logs
# Space complexity: O(M*N)
