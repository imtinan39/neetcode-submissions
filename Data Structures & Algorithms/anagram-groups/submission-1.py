class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictd={}
        for i in strs:
            result="".join(sorted(i))
            if result not in dictd:
                li=[]
                li.append(i)
                dictd[result]=li
            elif result in dictd:
                dictd[result].append(i)
        ans=[]
        for i in dictd.keys():
            ans.append(dictd[i])
        return ans

        