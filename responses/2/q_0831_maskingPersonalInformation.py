class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            # Email address
            name, domain = s.lower().split('@')
            masked_name = name[0] + '*****' + name[-1]
            return masked_name + '@' + domain
        else:
            # Phone number
            digits = ''.join(c for c in s if c.isdigit())
            local_number = '***-***-' + digits[-4:]
            if len(digits) == 10:
                return local_number
            country_code = '+' + '*' * (len(digits) - 10) + '-'
            return country_code + local_number
