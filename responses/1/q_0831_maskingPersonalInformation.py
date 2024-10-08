class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:  # Email address
            s = s.lower()
            name, domain = s.split('@')
            return f"{name[0]}{'*****'}{name[-1]}@{domain}"
        else:  # Phone number
            digits = [c for c in s if c.isdigit()]
            local_number = '***-***-' + ''.join(digits[-4:])
            if len(digits) == 10:
                return local_number
            country_code_length = len(digits) - 10
            country_code = '+' + '*' * country_code_length
            return f"{country_code}-{local_number}"