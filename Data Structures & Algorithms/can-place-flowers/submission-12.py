class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0
        flowerbed_1=[0] + flowerbed + [0]
        

        for i in range(1,len(flowerbed_1)-1):
            if flowerbed_1[i-1]==0 and flowerbed_1[i+1]==0 and flowerbed_1[i]==0:
                count+=1
                flowerbed_1[i]=1
        return count>=n
