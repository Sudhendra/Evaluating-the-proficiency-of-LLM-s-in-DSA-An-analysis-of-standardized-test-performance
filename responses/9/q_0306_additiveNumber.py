class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def is_valid_sequence(num, first, second):
            if not num:
                return True
            for i in range(1, len(num) + 1):
                if (len(str(first)) > 1 and str(first)[0] == "0") or (len(str(second)) > 1 and str(second)[0] == "0"):
                    return False
                third = int(num[:i])
                if third == first + second and is_valid_sequence(num[i:], second, third):
                    return True
            return False

        if not num or len(num) < 3:
            return False
        for i in range(1, len(num)):
            for j in range(i + 1, len(num)):
                first = int(num[:i])
                second = int(num[i:j])
                if (len(str(first)) > 1 and str(first)[0] == "0") or (len(str(second)) > 1 and str(second)[0] == "0"):
                    continue
                if is_valid_sequence(num[j:], first, second):
                    return True
        return False
