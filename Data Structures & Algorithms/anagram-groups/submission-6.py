class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for i in strs:
            sorted_s = ''.join(sorted(i))
            if sorted_s not in dic:
                dic[sorted_s]=[i]
            else:
                dic[sorted_s].append(i)
        print(dic)
        result=[]
        for i in dic.keys():
            result.append(dic[i])

        return result

        