from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_len = min(len(s) for s in strs)  # Find the length of the shortest string in the list

        for i in range(min_len):
            char = strs[0][i]  # Get the character to compare, starting from the first string
            for s in strs:
                if s[i] != char:  # Compare the character with the same position in other strings
                    return s[:i]  # Return the common prefix found so far
        return strs[0][:min_len]  # Return the common prefix based on the shortest string

# Example usage
solution = Solution()
result = solution.longestCommonPrefix(["flower","flow","flight"])
print(result)  # Output: "fl"
