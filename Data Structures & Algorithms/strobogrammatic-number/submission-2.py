class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        maps={"1":"1","6":"9","9":"6","8":"8","0":"0"}

        s=""
        for i in range(len(num)-1,-1,-1):
            if num[i] not in maps:
                return False
            else:
                s+="".join(maps[num[i]])
        print(s)
        return num==s