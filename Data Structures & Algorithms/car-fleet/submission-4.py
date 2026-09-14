class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # start with n car fleets and reduce them by 1 everytime a merge happend
        # 4 is faster than 7, is the speed larger than the distance 7 is from target?
            # 7 -> speed 1 => 3 rounds
            # 4 -> speed 2 => 3 rounds
            # rounds are the same, merge fleet
        # 1 is same speed as 4, never catch up, do not merge
        # 0 is slower than 1, never catch up

        times = []

        i = 0
        while i < len(position):
            position[i] = (position[i], speed[i])
            i += 1
        
        position.sort(reverse=True)
        
        for c in position:
            rounds = (target - c[0]) / c[1]
            if not times or rounds > times[-1]:
                times.append(rounds)
        
        return len(times)


        
        

        