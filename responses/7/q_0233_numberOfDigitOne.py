    def countDigitOne(self, n: int) -> int:
        ones_count = 0
        for i in range(n+1):
            ones_count += str(i).count('1')
        return ones_count
