class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        strs.sort()
        ln=min(len(strs[0]),len(strs[-1]))
        for i in range(ln):
            if strs[0][i]==strs[-1][i]:
                ans+=strs[0][i]
            else:
                break
        return ans
