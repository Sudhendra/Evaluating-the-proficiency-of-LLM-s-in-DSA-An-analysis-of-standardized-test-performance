class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        import collections

        positions = collections.defaultdict(list)
        for i, char in enumerate(ring):
            positions[char].append(i)

        memo = {}

        def dp(cur_pos, key_index):
            if key_index == len(key):
                return 0
            if (cur_pos, key_index) in memo:
                return memo[(cur_pos, key_index)]

            result = float('inf')
            for next_pos in positions[key[key_index]]:
                cur_steps = abs(cur_pos - next_pos)
                cur_steps = min(cur_steps, len(ring) - cur_steps)
                result = min(result, cur_steps + 1 + dp(next_pos, key_index + 1))

            memo[(cur_pos, key_index)] = result
            return result

        return dp(0, 0)  # Start from position 0 and key index 0
