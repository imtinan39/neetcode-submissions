class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        
        result = "".join(c for c in s if c.isalnum())
        r=len(result)-1
        result=result.lower()
        print(result)
        while l <= r:
            if result[l]!=result[r]:
                return False
            else:
                l+=1
                r-=1
        return True
        