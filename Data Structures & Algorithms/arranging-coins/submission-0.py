class Solution:
    def arrangeCoins(self, n: int) -> int:
        count=0
        i=1
        while n>0:
            if n>=i:
                count+=1
                n-=i
            else:
                break
            i+=1
                
        return count
        