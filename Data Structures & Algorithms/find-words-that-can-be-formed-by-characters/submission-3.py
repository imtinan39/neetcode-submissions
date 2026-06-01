class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        char={}
        count=0
        ans=0
        for i in chars:
            char[i]=char.get(i,0)+1

        for w in words:
            hashmap={}

            for ch in w:
                hashmap[ch]=hashmap.get(ch,0)+1
            
            for ch in w:
                if ch in char and hashmap[ch]>char[ch]:
                    break
                elif ch in char and hashmap[ch]<=char[ch]:
                    count+=1
            if count==len(w):
                ans+=count
                count=0
            else:
                count=0
        return ans

        