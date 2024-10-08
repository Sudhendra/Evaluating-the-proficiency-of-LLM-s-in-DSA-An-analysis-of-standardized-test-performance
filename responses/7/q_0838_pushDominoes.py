    def pushDominoes(self, dominoes: str) -> str:
        dominoes = 'L' + dominoes + 'R'
        result = []
        i = 0

        for j in range(1, len(dominoes)):
            if dominoes[j] == '.':
                continue

            middle_length = j - i - 1

            if i:
                result.append(dominoes[i])

            if dominoes[i] == dominoes[j]:
                result.append(dominoes[i] * middle_length)
            elif dominoes[i] == 'L' and dominoes[j] == 'R':
                result.append('.' * middle_length)
            else:
                result.append('R' * (middle_length // 2) + '.' * (middle_length % 2) + 'L' * (middle_length // 2))

            i = j

        return ''.join(result)
