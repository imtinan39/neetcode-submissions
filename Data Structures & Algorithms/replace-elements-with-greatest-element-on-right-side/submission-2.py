class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi=-1
        for i in range(len(arr)-1,-1,-1):
            new_maxi=max(arr[i],maxi)
            arr[i]=maxi
            maxi=new_maxi
        return arr
    
        