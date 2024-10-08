front_matter = {
    "qid": 2881,
    "title": "Create a New Column",
    "titleSlug": "create-a-new-column",
    "difficulty": "Easy",
    "tags": [],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
# This question has no Python code stub.
# Generating a generic Python code stub
class Solution:
    """
    ```
    DataFrame employees
    +-------------+--------+
    | Column Name | Type.  |
    +-------------+--------+
    | name        | object |
    | salary      | int.   |
    +-------------+--------+
    ```
    A company plans to provide its employees with a bonus.

    Write a solution to create a new column name `bonus` that contains the **doubled values** of the `salary` column.

    The result format is in the following example.



    **Example 1:**

    ```
    Input:
    DataFrame employees
    +---------+--------+
    | name    | salary |
    +---------+--------+
    | Piper   | 4548   |
    | Grace   | 28150  |
    | Georgia | 1103   |
    | Willow  | 6593   |
    | Finn    | 74576  |
    | Thomas  | 24433  |
    +---------+--------+
    Output:
    +---------+--------+--------+
    | name    | salary | bonus  |
    +---------+--------+--------+
    | Piper   | 4548   | 9096   |
    | Grace   | 28150  | 56300  |
    | Georgia | 1103   | 2206   |
    | Willow  | 6593   | 13186  |
    | Finn    | 74576  | 149152 |
    | Thomas  | 24433  | 48866  |
    +---------+--------+--------+
    Explanation:
    A new column bonus is created by doubling the value in the column salary.
    ```"""

    def createANewColumn(self) -> Any:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
