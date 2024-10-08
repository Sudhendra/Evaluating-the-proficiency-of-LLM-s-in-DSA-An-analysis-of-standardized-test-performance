class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = 'L' + dominoes + 'R'  # Add 'L' at the beginning and 'R' at the end to simplify edge cases
        result = []
        left = 0

        for right in range(1, len(dominoes)):
            if dominoes[right] == '.':
                continue

            middle = right - left - 1
            if left > 0:
                result.append(dominoes[left])

            if dominoes[left] == dominoes[right]:
                result.append(dominoes[left] * middle)
            elif dominoes[left] == 'L' and dominoes[right] == 'R':
                result.append('.' * middle)
            else:
                result.append('R' * (middle // 2) + '.' * (middle % 2) + 'L' * (middle // 2))

            left = right

        return ''.join(result)
