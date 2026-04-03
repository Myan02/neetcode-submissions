class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for op in operations:
            if op == "+":
                val_b = scores.pop()
                val_a = scores.pop()
                scores.append(val_a)
                scores.append(val_b)
                scores.append(val_a + val_b)

            elif op == "D":
                top = scores[-1]
                scores.append(2 * top)
                
            elif op == "C":
                scores.pop()

            else:
                scores.append(int(op))
        
        return sum(scores)
        