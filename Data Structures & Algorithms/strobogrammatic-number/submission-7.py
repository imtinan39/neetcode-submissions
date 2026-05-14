class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        maps={"1":"1","6":"9","9":"6","8":"8","0":"0"}

        l=0
        r=len(num)-1
        while l<=r:
            if num[r] in maps and maps[num[r]]==num[l]:
                r-=1
                l+=1
            else:
                return False
        return True