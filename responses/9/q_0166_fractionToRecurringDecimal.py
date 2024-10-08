class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = ""
        if numerator * denominator < 0:
            res += "-"
        numerator, denominator = abs(numerator), abs(denominator)
        res += str(numerator // denominator)
        rem = numerator % denominator
        if rem == 0:
            return res
        res += "."
        hashmap = {}
        while rem:
            if rem in hashmap:
                res = res[:hashmap[rem]] + "(" + res[hashmap[rem]:] + ")"
                break
            hashmap[rem] = len(res)
            rem *= 10
            res += str(rem // denominator)
            rem %= denominator
        return res
