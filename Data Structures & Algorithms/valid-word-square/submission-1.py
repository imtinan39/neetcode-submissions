class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        hashmap={}
        for w in range(len(words)):
            for i in range(len(words[w])):
                hashmap[i]=hashmap.get(i,"")+words[w][i]
        
        
        for w in range(len(words)):
            if words[w]==hashmap.get(w,""):
                continue
            else:
                return False
        return True
        