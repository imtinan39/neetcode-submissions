class Solution:
    def confusingNumber(self, n: int) -> bool:
        hashmap={"0":"0","1":"1","2":"i","3":"i","4":"i","5":"i","6":"9","7":"i","8":"8","9":"6"}

        s=str(n)
        k=""

        for i in range(len(s)-1,-1,-1):
            if hashmap[s[i]]=="i":
                return False
            else:
                k+=hashmap[s[i]]
        
        if int(k)!=n:
            return True
        else:
            return False

        