from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, path, parts):
            # Base case: if we have found a valid IP address
            if len(path) == 4 and start == len(s):
                result.append(".".join(path))
                return
            # Invalid case: if we have used all digits but there are less than 4 parts
            if len(path) == 4 or start == len(s):
                return
            # Recursive case: try all possible splits
            for i in range(1, 4):
                # Extract current part by slicing the string
                if start + i > len(s):
                    break
                part = s[start: start + i]
                # Check for leading zeros and out of range values
                if (len(part) > 1 and part[0] == '0') or int(part) > 255:
                    continue
                # Recurse with the updated start index, current part, and parts list
                backtrack(start + i, path + [part], parts + 1)
        
        result = []
        backtrack(0, [], 0)
        return result
