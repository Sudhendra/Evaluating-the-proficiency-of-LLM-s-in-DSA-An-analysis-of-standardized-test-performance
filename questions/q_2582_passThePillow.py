front_matter = {
    "qid": 2582,
    "title": "Pass the Pillow",
    "titleSlug": "pass-the-pillow",
    "difficulty": "Easy",
    "tags": ["Math", "Simulation"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """There are `n` people standing in a line labeled from `1` to `n`. The first person in the line is holding a pillow initially. Every second, the person holding the pillow passes it to the next person standing in the line. Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.

    * For example, once the pillow reaches the `n^{th}` person they pass it to the `n - 1^{th}` person, then to the `n - 2^{th}` person and so on.

    Given the two positive integers `n` and `time`, return *the index of the person holding the pillow after* `time` *seconds*.



    **Example 1:**

    ```
    Input: n = 4, time = 5
    Output: 2
    Explanation: People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 3 -> 2.
    Afer five seconds, the pillow is given to the 2^{nd} person.
    ```
    **Example 2:**

    ```
    Input: n = 3, time = 2
    Output: 3
    Explanation: People pass the pillow in the following way: 1 -> 2 -> 3.
    Afer two seconds, the pillow is given to the 3^{r}^{d} person.
    ```


    **Constraints:**

    * `2 <= n <= 1000`
    * `1 <= time <= 1000`
    """

    def passThePillow(self, n: int, time: int) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
