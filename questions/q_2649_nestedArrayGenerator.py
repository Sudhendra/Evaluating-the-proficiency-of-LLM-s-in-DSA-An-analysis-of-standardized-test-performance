front_matter = {
    "qid": 2649,
    "title": "Nested Array Generator",
    "titleSlug": "nested-array-generator",
    "difficulty": "Medium",
    "tags": [],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
# This question has no Python code stub.
# Generating a generic Python code stub
class Solution:
    """Given a **multi-dimensional array** of integers, return a generator object which yields integers in the same order as **inorder traversal**.

    A **multi-dimensional array** is a recursive data structure that contains both integers and other **multi-dimensional arrays**.

    **inorder traversal** iterates over each array from left to right, yielding any integers it encounters or applying **inorder traversal** to any arrays it encounters.



    **Example 1:**

    ```
    Input: arr = [[[6]],[1,3],[]]
    Output: [6,1,3]
    Explanation:
    const generator = inorderTraversal(arr);
    generator.next().value; // 6
    generator.next().value; // 1
    generator.next().value; // 3
    generator.next().done; // true
    ```
    **Example 2:**

    ```
    Input: arr = []
    Output: []
    Explanation: There are no integers so the generator doesn't yield anything.
    ```


    **Constraints:**

    * `0 <= arr.flat().length <= 10^{5}`
    * `0 <= arr.flat()[i] <= 10^{5}`
    * `maxNestingDepth <= 10^{5}`



    **Can you solve this without creating a new flattened version of the array?**"""

    def nestedArrayGenerator(self) -> Any:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
