front_matter = {
    "qid": 633,
    "title": "Sum of Square Numbers",
    "titleSlug": "sum-of-square-numbers",
    "difficulty": "Medium",
    "tags": ["Math", "Two Pointers", "Binary Search"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given a non-negative integer `c`, decide whether there're two integers `a` and `b` such that `a^{2} + b^{2} = c`.

    """

    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(c ** 0.5)
        while left <= right:
            current_sum = left * left + right * right
            if current_sum == c:
                return True
            elif current_sum < c:
                left += 1
            else:
                right -= 1
        return False