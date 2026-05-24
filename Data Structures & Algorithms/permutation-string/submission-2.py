class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        dq=deque(maxlen=len(s1))
        l=0
        count=0

        for  r in range(len(s2)):
            dq.append(s2[r])

            if len(dq)==len(s1):
                if str(sorted(s1))==str(sorted(dq)):
                    return True
        return False
        