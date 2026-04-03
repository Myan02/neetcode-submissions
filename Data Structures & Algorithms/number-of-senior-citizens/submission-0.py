class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0

        # iterate through each detail
        for detail in details:
            age = detail[-4:-2] # parse data to get age
            count = count + 1 if int(age) > 60 else count   # check if age is over 60
        
        return count

        