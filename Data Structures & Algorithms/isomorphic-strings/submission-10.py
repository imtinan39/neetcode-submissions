class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_st = {}
        used_t = {}

        for i in range(len(s)):
            if s[i] not in map_st and t[i] not in used_t:
                map_st[s[i]] = t[i]
                used_t[t[i]] = True
            elif s[i] not in map_st or map_st[s[i]] != t[i]:
                return False

        return True