class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count = {'L': 0, 'R': 0, 'U': 0, 'D': 0}
        for move in moves:
            count[move] += 1
        return count['L'] == count['R'] and count['U'] == count['D']
