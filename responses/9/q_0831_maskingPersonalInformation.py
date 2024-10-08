class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            s = s.lower()
            name, domain = s.split('@')
            return name[0] + "*****" + name[-1] + "@" + domain
        else:
            digits = ''.join(filter(str.isdigit, s))
            local = "***-***-" + digits[-4:]
            if len(digits) == 10:
                return local
            return "+" + "*" * (len(digits) - 10) + "-***-***-" + digits[-4:]

