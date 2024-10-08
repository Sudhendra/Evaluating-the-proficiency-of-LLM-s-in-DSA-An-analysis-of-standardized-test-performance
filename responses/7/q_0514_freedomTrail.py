class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        def dp(index_ring, index_key):
            if index_key == len(key):
                return 0
            if (index_ring, index_key) in memo:
                return memo[(index_ring, index_key)]

            result = float('inf')
            for next_index_ring in char_to_index[key[index_key]]:
                clock_wise = abs(next_index_ring - index_ring)
                anti_clock_wise = len(ring) - clock_wise
                result = min(result, min(clock_wise, anti_clock_wise) + 1 + dp(next_index_ring, index_key + 1))

            memo[(index_ring, index_key)] = result
            return result

        char_to_index = {}
        for i, char in enumerate(ring):
            if char not in char_to_index:
                char_to_index[char] = []
            char_to_index[char].append(i)

        memo = {}
        return dp(0, 0)
