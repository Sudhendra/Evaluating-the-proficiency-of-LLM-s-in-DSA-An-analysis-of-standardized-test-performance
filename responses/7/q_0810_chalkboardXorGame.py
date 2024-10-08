from typing import List

class Solution:
    """You are given an array of integers `nums` represents the numbers written on a chalkboard.

    Alice and Bob take turns erasing exactly one number from the chalkboard, with Alice starting first. If erasing a number causes the bitwise XOR of all the elements of the chalkboard to become `0`, then that player loses. The bitwise XOR of one element is that element itself, and the bitwise XOR of no elements is `0`.

    Also, if any player starts their turn with the bitwise XOR of all the elements of the chalkboard equal to `0`, then that player wins.

    Return `true` *if and only if Alice wins the game, assuming both players play optimally*.
    """

    def xorGame(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0 or self.xor(nums) == 0:
            return True
        return False

    def xor(self, nums: List[int]) -> int:
        xor_val = 0
        for num in nums:
            xor_val ^= num
        return xor_val
