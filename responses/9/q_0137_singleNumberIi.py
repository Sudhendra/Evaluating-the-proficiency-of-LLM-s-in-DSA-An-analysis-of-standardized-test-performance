front_matter = {
    "qid": 137,
    "title": "Single Number II",
    "titleSlug": "single-number-ii",
    "difficulty": "Medium",
    "tags": ["Array", "Bit Manipulation"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = twos = 0
        
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        
        return ones