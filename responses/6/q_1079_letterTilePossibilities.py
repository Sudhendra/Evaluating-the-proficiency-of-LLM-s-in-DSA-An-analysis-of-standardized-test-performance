class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(count):
            total = 0
            for i in range(len(count)):
                if count[i] == 0:
                    continue
                total += 1  # Count the empty string
                count[i] -= 1
                total += backtrack(count)
                count[i] += 1
            return total

        count = [0] * 26
        for tile in tiles:
            count[ord(tile) - ord('A')] += 1

        return backtrack(count)
