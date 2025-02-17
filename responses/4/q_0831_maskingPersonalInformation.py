class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:  # Email address
            name, domain = s.lower().split('@')
            return name[0] + '*****' + name[-1] + '@' + domain
        else:  # Phone number
            digits = ''.join([c for c in s if c.isdigit()])
            local_number = '***-***-' + digits[-4:]
            if len(digits) == 10:
                return local_number
            else:
                country_code = '+' + '*' * (len(digits) - 10) + '-'
                return country_code + local_number
