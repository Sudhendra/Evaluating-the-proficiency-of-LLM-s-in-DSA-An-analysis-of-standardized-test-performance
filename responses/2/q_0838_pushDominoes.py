class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = 'L' + dominoes + 'R'
        result = []
        left, right = 0, 1

        for right in range(1, len(dominoes)):
            if dominoes[right] == '.':
                continue

            length = right - left - 1

            if left:
                result.append(dominoes[left])

            if dominoes[left] == dominoes[right]:
                result.append(dominoes[left] * length)
            elif dominoes[left] == 'L' and dominoes[right] == 'R':
                result.append('.' * length)
            else:
                result.append('R' * (length // 2) + '.' * (length % 2) + 'L' * (length // 2))

            left = right

        return ''.join(result)