class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            local_part, domain = s.lower().split('@')
            return local_part[0] + '*****' + local_part[-1] + '@' + domain
        else:
            digits = ''.join(filter(str.isdigit, s))
            local_number = '***-***-' + digits[-4:]
            if len(digits) == 10:
                return local_number
            else:
                return '+' + '*' * (len(digits) - 10) + '-' + local_number
