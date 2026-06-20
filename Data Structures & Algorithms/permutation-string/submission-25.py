class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        hash_s1 = {}
        hash_s2 = {}

        for ch in s1:
            hash_s1[ch] = hash_s1.get(ch, 0) + 1

        for r in range(len(s2)):
            hash_s2[s2[r]] = hash_s2.get(s2[r], 0) + 1

            if r - l + 1 == len(s1):
                if hash_s2 == hash_s1:
                    return True

                hash_s2[s2[l]] -= 1
                if hash_s2[s2[l]] == 0:
                    del hash_s2[s2[l]]
                l += 1

        return False
        