front_matter = {
    "qid": 2332,
    "title": "The Latest Time to Catch a Bus",
    "titleSlug": "the-latest-time-to-catch-a-bus",
    "difficulty": "Medium",
    "tags": ["Array", "Two Pointers", "Binary Search", "Sorting"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given a **0-indexed** integer array `buses` of length `n`, where `buses[i]` represents the departure time of the `i^{th}` bus. You are also given a **0-indexed** integer array `passengers` of length `m`, where `passengers[j]` represents the arrival time of the `j^{th}` passenger. All bus departure times are unique. All passenger arrival times are unique.

    You are given an integer `capacity`, which represents the **maximum** number of passengers that can get on each bus.

    When a passenger arrives, they will wait in line for the next available bus. You can get on a bus that departs at `x` minutes if you arrive at `y` minutes where `y <= x`, and the bus is not full. Passengers with the **earliest** arrival times get on the bus first.

    More formally when a bus arrives, either:

    * If `capacity` or fewer passengers are waiting for a bus, they will **all** get on the bus, or
    * The `capacity` passengers with the **earliest** arrival times will get on the bus.

    Return *the latest time you may arrive at the bus station to catch a bus*. You **cannot** arrive at the same time as another passenger.

    **Note:** The arrays `buses` and `passengers` are not necessarily sorted.



    **Example 1:**

    ```
    Input: buses = [10,20], passengers = [2,17,18,19], capacity = 2
    Output: 16
    Explanation: Suppose you arrive at time 16.
    At time 10, the first bus departs with the 0^{th} passenger.
    At time 20, the second bus departs with you and the 1^{st} passenger.
    Note that you may not arrive at the same time as another passenger, which is why you must arrive before the 1^{st} passenger to catch the bus.
    ```
    **Example 2:**

    ```
    Input: buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2
    Output: 20
    Explanation: Suppose you arrive at time 20.
    At time 10, the first bus departs with the 3^{rd} passenger.
    At time 20, the second bus departs with the 5^{th} and 1^{st} passengers.
    At time 30, the third bus departs with the 0^{th} passenger and you.
    Notice if you had arrived any later, then the 6^{th} passenger would have taken your seat on the third bus.
    ```


    **Constraints:**

    * `n == buses.length`
    * `m == passengers.length`
    * `1 <= n, m, capacity <= 10^{5}`
    * `2 <= buses[i], passengers[i] <= 10^{9}`
    * Each element in `buses` is **unique**.
    * Each element in `passengers` is **unique**.
    """

    def latestTimeCatchTheBus(
        self, buses: List[int], passengers: List[int], capacity: int
    ) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
