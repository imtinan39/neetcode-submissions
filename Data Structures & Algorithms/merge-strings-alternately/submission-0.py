class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        mini=min(len(word1),len(word2))
        for i in range(mini):
            s+=word1[i]
            s+=word2[i]
        
        if len(word1)>len(word2):
            s+=word1[mini:len(word1)]
        else:
            s+=word2[mini:len(word2)]
        return s

