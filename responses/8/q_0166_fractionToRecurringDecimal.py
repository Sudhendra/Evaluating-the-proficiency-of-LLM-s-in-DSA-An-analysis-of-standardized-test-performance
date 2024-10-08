class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)

        res = []

        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        res.append(str(numerator // denominator))
        res.append(".")

        pos = {}
        remainder = numerator % denominator
        while remainder != 0:
            if remainder in pos:
                res.insert(pos[remainder], "(")
                res.append(")")
                break

            pos[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(res)
