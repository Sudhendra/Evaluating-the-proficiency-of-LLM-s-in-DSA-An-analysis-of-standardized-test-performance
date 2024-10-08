class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s = s.lower()
            name, domain = s.split('@')
            masked_name = name[0].lower() + '*****' + name[-1].lower()
            return masked_name + '@' + domain
        else:
            digits = ''.join(filter(str.isdigit, s))
            local_num = '***-***-' + digits[-4:]
            if len(digits) == 10:
                return local_num
            country_code = '*' * (len(digits) - 10) + '-'
            return '+' + country_code + local_num