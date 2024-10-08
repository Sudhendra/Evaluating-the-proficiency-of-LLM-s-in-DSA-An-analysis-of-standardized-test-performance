class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            return self.mask_email(s)
        else:
            return self.mask_phone_number(s)

    def mask_email(self, email: str) -> str:
        name, domain = email.split('@')
        return name[0].lower() + "*****" + name[-1].lower() + "@" + domain.lower()

    def mask_phone_number(self, phone: str) -> str:
        digits = [c for c in phone if c.isdigit()]
        local_number = "***-***-" + "".join(digits[-4:])
        if len(digits) == 10:
            return local_number
        else:
            country_code = "+"
            country_code += "*" * (len(digits) - 10)
            return f"{country_code}-{local_number}"
