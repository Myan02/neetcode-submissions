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
                if (total[0] < 3 and total[1] < 1) or (total[0] < 1 and total[1] >= 1):
                    return False
                
                if total[1] >= 1:
                    total[0] -= 1
                    total[1] -= 1
                else:
                    total[0] -= 3
                
                total[2] += 1
        
        return True
                    

                
                
        