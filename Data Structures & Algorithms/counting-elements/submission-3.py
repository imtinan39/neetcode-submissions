class Solution:
    def countElements(self, arr: List[int]) -> int:
        se=set(arr)
        count=0
        for i in arr:
            if i+1 in se:
                count+=1
        return count
        