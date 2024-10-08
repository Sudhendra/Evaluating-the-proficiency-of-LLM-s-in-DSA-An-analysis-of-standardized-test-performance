class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n ** 0.5)  # The number of bulbs that are on will be the square root of n since a bulb changes its state only at those positions which are perfect squares.