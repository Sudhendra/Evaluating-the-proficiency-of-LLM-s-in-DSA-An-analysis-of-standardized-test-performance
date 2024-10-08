class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        if a > b:
            return self.helper('a', 'b', a, b)
        else:
            return self.helper('b', 'a', b, a)

    def helper(self, char1, char2, count1, count2):
        result = ''
        while count1 > 0 or count2 > 0:
            if count1 > 0:
                result += char1
                count1 -= 1
                if count1 > count2:
                    result += char1
                    count1 -= 1
            if count2 > 0:
                result += char2
                count2 -= 1
        return result