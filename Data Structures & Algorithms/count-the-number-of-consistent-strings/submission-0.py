class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        count=0

        for i in words:
            tmp=0
            for w in i:
                if w in allowed:
                    tmp+=1
                else:
                    break
            if tmp==len(i):
                count+=1
        return count
            
        