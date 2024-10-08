class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        stones = [a, b, c]
        stones.sort()
        
        diff1 = stones[1] - stones[0] - 1
        diff2 = stones[2] - stones[1] - 1
        
        if diff1 == 0 and diff2 == 0:
            return [0, 0]
        elif (diff1 <= 1 or diff2 <= 1):
            return [1, diff1 + diff2]
        else:
            return [2, diff1 + diff2]
