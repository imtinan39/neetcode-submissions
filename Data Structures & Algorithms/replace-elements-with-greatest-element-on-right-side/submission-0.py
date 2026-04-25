class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi=-1
        hashmap={}
        for i in range(len(arr)-2,-1,-1):
            maxi=max(arr[i+1],maxi)
            hashmap[i]=maxi
        hashmap[len(arr)-1]=-1

        for i in hashmap.keys():
            arr[i]=hashmap[i]
        return arr
    
        