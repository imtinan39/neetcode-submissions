class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        first=0
        sec=0
        count=0
        g.sort()
        s.sort()

        while first<len(g) and sec<len(s):
            if g[first]<=s[sec]:
                count+=1
                first+=1
                sec+=1
            else:
                sec+=1
        return count

        