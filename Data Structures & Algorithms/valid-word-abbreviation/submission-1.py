class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i=0
        j=0

        while i<len(word) and j < len(abbr):

            if word[i]==abbr[j]:
                i=i+1
                j=j+1
            elif (abbr[j].isdigit()==False and word[i]!=abbr[j]) or abbr[j]=="0":
                return False
            elif abbr[j].isdigit():
                num=""
                while j<len(abbr) and abbr[j].isdigit():
                    num+=abbr[j]
                    j=j+1
                
                i=i+int(num)
        return i==len(word) and j==len(abbr)
                    


        