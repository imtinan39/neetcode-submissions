class Solution:
    def maxDifference(self, s: str) -> int:
        count=[0]*26

        for i in s:
            count[ord(i)-ord("a")]+=1
        odd=[]
        even=[]

        for i in count:
            if i!=0 and i%2==0:
                even.append(i)
            elif i%2!=0:
                odd.append(i)
        return max(odd)-min(even)
        


        