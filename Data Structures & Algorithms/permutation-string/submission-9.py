class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        dq=deque(maxlen=len(s1))
        l=0
        count=0
        p=str(sorted(s1))

        for  r in range(len(s2)):

            if s2[r] in s1:
                dq.append(s2[r])
            else:
                dq=deque(maxlen=len(s1))

            
            if len(dq)==len(s1):
                if p==str(sorted(dq)):
                    return True
        return False
        