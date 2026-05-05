class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        net = 0
        for direction, amount in shift:
            if direction == 0:   # left
                net += amount
            else:                # right
                net -= amount
        
        net %= len(s)
        return  s[net:]+s[:net] if net else s

                

        