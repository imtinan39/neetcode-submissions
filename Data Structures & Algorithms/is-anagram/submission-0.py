class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_1={}
        dict_2={}
        if len(s)!=len(t):
            return False
        else:
            for i in range(len(s)):
                dict_1[s[i]]=dict_1.get(s[i],0)+1
                dict_2[t[i]]=dict_2.get(t[i],0)+1
            if dict_1==dict_2:
                return True
            else:
                return False
