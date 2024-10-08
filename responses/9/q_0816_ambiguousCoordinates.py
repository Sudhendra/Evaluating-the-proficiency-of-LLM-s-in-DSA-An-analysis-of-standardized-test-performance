class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def is_valid_num(num_str):
            if num_str.startswith('0') and num_str != '0':
                return False
            if '.' in num_str:
                left, right = num_str.split('.')
                return (not left.startswith('0') or left == '0') and (not right.endswith('0'))
            return True
        
        def get_valid_nums(num_str):
            if is_valid_num(num_str):
                yield num_str
            for i in range(1, len(num_str)):
                left_num = num_str[:i]
                right_num = num_str[i:]
                if is_valid_num(left_num) and is_valid_num(right_num):
                    yield f"{left_num}.{right_num}" if right_num else left_num
        
        s = s[1:-1]
        n = len(s)
        results = []
        
        for i in range(1, n):
            for left_num in get_valid_nums(s[:i]):
                for right_num in get_valid_nums(s[i:]):
                    results.append(f"({left_num}, {right_num})")
        
        return results
