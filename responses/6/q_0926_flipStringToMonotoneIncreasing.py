class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # Count number of 1's and initial number of flips needed for entire string to be 1's
        ones_count = s.count('1')
        flips = ones_count
        # Initialize current flips needed for making substring ending at each index monotonically increasing
        current_flips = 0

        for char in s:
            if char == '0':
                # If current character is '0', we need to flip it to '1', so increment flips count
                current_flips += 1
            else:
                # If current character is '1', it can be part of 1's group or start of 0's group
                # To make this char part of 0's group, we increment current_flips
                current_flips = min(current_flips, flips)
                # Update total flips count based on minimum flips needed so far
                flips = min(flips, current_flips)

        return flips
