class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n**0.5)  # The number of bulbs that remain on is equal to the number of perfect squares less than or equal to n.