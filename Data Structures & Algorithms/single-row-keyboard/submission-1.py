class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hashmap={}

        for i in range(len(keyboard)):
            hashmap[keyboard[i]]=i
        p=0
        count=0
        for i in word:
            count+=abs(p-hashmap[i])
            p=hashmap[i]
        return count
        