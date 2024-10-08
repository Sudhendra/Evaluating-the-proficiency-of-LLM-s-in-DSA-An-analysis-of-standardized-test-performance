class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:  # Email
            name, domain = s.lower().split('@')
            return name[0] + '*****' + name[name.find('@') - 1:] + '@' + domain
        else:  # Phone number
            digits = ''.join(filter(str.isdigit, s))
            local_num = '***-***-' + digits[-4:]
            if len(digits) == 10:
                return local_num
            else:
                return '+' + '*' * (len(digits) - 10) + '-' + local_num

# Test cases
solution = Solution()
print(solution.maskPII("LeetCode@LeetCode.com"))  # Output: "l*****e@leetcode.com"
print(solution.maskPII("AB@qq.com"))  # Output: "a*****b@qq.com"
print(solution.maskPII("1(234)567-890"))  # Output: "***-***-7890"
