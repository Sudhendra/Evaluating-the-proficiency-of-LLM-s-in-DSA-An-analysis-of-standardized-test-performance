front_matter = {
    "qid": 878,
    "title": "Nth Magical Number",
    "titleSlug": "nth-magical-number",
    "difficulty": "Hard",
    "tags": ["Math", "Binary Search"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """A positive integer is *magical* if it is divisible by either `a` or `b`.

    Given the three integers `n`, `a`, and `b`, return the `n^{th}` magical number. Since the answer may be very large, **return it modulo** `10^{9} + 7`.

    **Example 1:**

    ```
    Input: n = 1, a = 2, b = 3
    Output: 2
    ```
    **Example 2:**

    ```
    Input: n = 4, a = 2, b = 3
    Output: 6
    ```

    **Constraints:**

    * `1 <= n <= 10^{9}`
    * `2 <= a, b <= 4 * 10^{4}`
    """

    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return a * b // gcd(a, b)

        mod = 10**9 + 7
        left, right = 2, 10**15
        while left < right:
            mid = (left + right) // 2
            if mid // a + mid // b - mid // lcm(a, b) < n:
                left = mid + 1
            else:
                right = mid
        return left % mod