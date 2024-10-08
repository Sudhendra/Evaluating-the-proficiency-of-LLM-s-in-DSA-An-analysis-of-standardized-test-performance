front_matter = {
    "qid": 1094,
    "title": "Car Pooling",
    "titleSlug": "car-pooling",
    "difficulty": "Medium",
    "tags": ["Array", "Sorting", "Heap (Priority Queue)", "Simulation", "Prefix Sum"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """There is a car with `capacity` empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

    You are given the integer `capacity` and an array `trips` where `trips[i] = [numPassengersi, fromi, toi]` indicates that the `i^{th}` trip has `numPassengersi` passengers and the locations to pick them up and drop them off are `fromi` and `toi` respectively. The locations are given as the number of kilometers due east from the car's initial location.

    Return `true` *if it is possible to pick up and drop off all passengers for all the given trips, or* `false` *otherwise*.



    **Example 1:**

    ```
    Input: trips = [[2,1,5],[3,3,7]], capacity = 4
    Output: false
    ```
    **Example 2:**

    ```
    Input: trips = [[2,1,5],[3,3,7]], capacity = 5
    Output: true
    ```


    **Constraints:**

    * `1 <= trips.length <= 1000`
    * `trips[i].length == 3`
    * `1 <= numPassengersi <= 100`
    * `0 <= fromi < toi <= 1000`
    * `1 <= capacity <= 10^{5}`
    """

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
