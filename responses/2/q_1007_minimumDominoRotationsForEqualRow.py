class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        
        # Helper function to calculate number of rotations required for a specific value
        def check(value):
            top_rotations = 0
            bottom_rotations = 0
            for i in range(n):
                if tops[i] != value and bottoms[i] != value:
                    return -1
                if tops[i] != value:
                    top_rotations += 1
                if bottoms[i] != value:
                    bottom_rotations += 1
            return min(top_rotations, bottom_rotations)
        
        # Check if it's possible to make all values in tops or bottoms equal by checking each value from 1 to 6
        rotations = check(tops[0])
        if rotations != -1 or tops[0] == bottoms[0]:
            return rotations
        else:
            return check(bottoms[0])
        
        return -1