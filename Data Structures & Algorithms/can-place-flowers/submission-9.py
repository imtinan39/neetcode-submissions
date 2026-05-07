class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0
        flowerbed_1=[]
        flowerbed_1.append(0)
        for i in flowerbed:
            flowerbed_1.append(i)
        flowerbed_1.append(0)

        for i in range(1,len(flowerbed_1)-1):
            if flowerbed_1[i-1]==0 and flowerbed_1[i+1]==0 and flowerbed_1[i]==0:
                count+=1
                flowerbed_1[i]=1
        return count>=n
