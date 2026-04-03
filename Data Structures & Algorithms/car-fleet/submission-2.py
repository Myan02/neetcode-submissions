class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # end case, when n cars reach the target, return the number of cars that didnt, plus 1
        fleets = []
        cars = [[p, s] for p, s in zip(position, speed)]
        cars.sort(key=lambda x: x[0], reverse=True)
        
        for p, s in cars:
            time = (target - p) / s
            if not fleets:
                fleets.append(time)
            elif time > fleets[-1]:
                fleets.append(time)
        
        return len(fleets)
            
        


        