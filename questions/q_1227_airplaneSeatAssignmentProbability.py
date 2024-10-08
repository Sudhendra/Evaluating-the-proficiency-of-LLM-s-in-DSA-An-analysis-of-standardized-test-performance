front_matter = {
    "qid": 1227,
    "title": "Airplane Seat Assignment Probability",
    "titleSlug": "airplane-seat-assignment-probability",
    "difficulty": "Medium",
    "tags": [
        "Math",
        "Dynamic Programming",
        "Brainteaser",
        "Probability and Statistics",
    ],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """`n` passengers board an airplane with exactly `n` seats. The first passenger has lost the ticket and picks a seat randomly. But after that, the rest of the passengers will:

    * Take their own seat if it is still available, and
    * Pick other seats randomly when they find their seat occupied

    Return *the probability that the* `n^{th}` *person gets his own seat*.



    **Example 1:**

    ```
    Input: n = 1
    Output: 1.00000
    Explanation: The first person can only get the first seat.
    ```
    **Example 2:**

    ```
    Input: n = 2
    Output: 0.50000
    Explanation: The second person has a probability of 0.5 to get the second seat (when first person gets the first seat).
    ```


    **Constraints:**

    * `1 <= n <= 10^{5}`
    """

    def nthPersonGetsNthSeat(self, n: int) -> float:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
