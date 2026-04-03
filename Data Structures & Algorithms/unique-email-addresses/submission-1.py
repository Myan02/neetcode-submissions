class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for email in emails:
            at_symbol = email.index("@")
            domain = email[at_symbol:]
            local = email[:at_symbol].replace(".", "")

            if "+" in local:
                plus_symbol = local.index("+")
                local = local[:plus_symbol]
            
            email = local + domain
            if email not in unique:
                unique.add(email)
        
        return len(unique)
            
            
