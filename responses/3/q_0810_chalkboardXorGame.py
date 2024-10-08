class Solution:
    """You are given an array of integers `nums` represents the numbers written on a chalkboard.

    Alice and Bob take turns erasing exactly one number from the chalkboard, with Alice starting first. If erasing a number causes the bitwise XOR of all the elements of the chalkboard to become `0`, then that player loses. The bitwise XOR of one element is that element itself, and the bitwise XOR of no elements is `0`.

    Also, if any player starts their turn with the bitwise XOR of all the elements of the chalkboard equal to `0`, then that player wins.

    Return `true` *if and only if Alice wins the game, assuming both players play optimally*.
    """

    def xorGame(self, nums: List[int]) -> bool:
        # Alice wins if and only if:
        # 1. The length of nums is even or
        # 2. The XOR of all elements of nums is 0

        return len(nums) % 2 == 0 or reduce(xor, nums) == 0
