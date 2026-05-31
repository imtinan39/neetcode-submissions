from typing import List
from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        dq = deque(students)
        r = 0
        rotations = 0

        while dq and r < len(sandwiches):
            if dq[0] == sandwiches[r]:
                dq.popleft()
                r += 1
                rotations = 0
            else:
                dq.append(dq.popleft())
                rotations += 1

                if rotations == len(dq):
                    break

        return len(dq)