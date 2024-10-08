from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]  # If no element is greater than target, return the first element

# Test cases
sol = Solution()
print(sol.nextGreatestLetter(["c", "f", "j"], "a"))  # Output: "c"
print(sol.nextGreatestLetter(["c", "f", "j"], "c"))  # Output: "f"
print(sol.nextGreatestLetter(["x", "x", "y", "y"], "z"))  # Output: "x"
