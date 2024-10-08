from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_len = min(len(s) for s in strs)
        low, high = 1, min_len

        def is_common_prefix(length: int) -> bool:
            prefix = strs[0][:length]
            return all(s.startswith(prefix) for s in strs)

        while low <= high:
            mid = (low + high) // 2
            if is_common_prefix(mid):
                low = mid + 1
            else:
                high = mid - 1

        return strs[0][:high]

# Test cases
solution = Solution()
assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""
