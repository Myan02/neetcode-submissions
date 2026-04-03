class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # total = [0, 0, 0]
        # total[i] where i equals number of i bills we have
        total = [0] * 3

        for customer in range(len(bills)):
            # collect 5 dollar bill
            if bills[customer] == 5:
                total[0] += 1
            elif bills[customer] == 10:
                
                # need 5 dollar bill for change
                if total[0] == 0:
                    return False
                
                total[0] -= 1
                total[1] += 1
            
            else:
                # need either 1 ten and 1 five or 3 fives
                if (total[0] < 3 and total[1] < 1) or (total[0] < 1 and total[1] >= 1):
                    return False
                
                # have a 10, so we should also have at least a 5
                if total[1] >= 1:
                    total[0] -= 1
                    total[1] -= 1
                
                # dont have a 10, need 3 fives
                else:
                    total[0] -= 3
                
                total[2] += 1
        
        return True
                    

                
                
        