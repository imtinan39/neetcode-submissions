class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic=defaultdict(list)

        for s in strs:
            count=[0]*26
            for c in s:
                res= ord(c)-ord("a")
                count[res]+=1
            dic[tuple(count)].append(s)
        return list(dic.values())