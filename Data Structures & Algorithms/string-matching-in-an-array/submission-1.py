import re
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        arr=set()
        for i in words:
            for j in words:
                if i!=j and j in i:
                    arr.add(j)
        return list(arr)
        