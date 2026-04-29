class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=""

        strs=sorted(strs)
        print(strs)
        rang=min(len(strs[0]),len(strs[-1]))
        print(rang)

        for i in range(rang):
            if strs[0][i]==strs[-1][i]:
                result+=strs[0][i]
            else:
                return result
        return result
        