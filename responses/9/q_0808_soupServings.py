front_matter = {
    "qid": 808,
    "title": "Soup Servings",
    "titleSlug": "soup-servings",
    "difficulty": "Medium",
    "tags": ["Math", "Dynamic Programming", "Probability and Statistics"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
import functools
class Solution:
    def soupServings(self, N: int) -> float:
        @functools.lru_cache(None)
        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            return 0.25 * (dp(a-100, b) + dp(a-75, b-25) + dp(a-50, b-50) + dp(a-25, b-75))
        
        if N > 4800:
            return 1.0
        return dp(N, N)
