class Solution:

    def maskPII(self, s: str) -> str:
        if '@' in s:
            lower_s = s.lower()
            name, domain = lower_s.split('@')
            return name[0] + '*****' + name[-1] + "@" + domain
        else:
            digits = ''.join(filter(str.isdigit, s))
            local_num = "***-***-" + digits[-4:]
            if len(digits) == 10:
                return local_num
            else:
                country_code = '+' + '*' * (len(digits) - 10) + '-'
                return country_code + local_num

    def another_solution(self, s: str) -> str:
        # Another solution can be added here

    def one_more_solution(self, s: str) -> str:
        # Another solution can be added here
