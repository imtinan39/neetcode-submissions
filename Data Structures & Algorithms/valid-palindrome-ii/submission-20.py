class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(l,r):
            while l<r:
                if s[l]!= s[r]:
                    return False
                l+=1
                r-=1
            return True
        l=0
        r=len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:

                if is_palindrome(l+1,r):
                    return True
                if is_palindrome(l,r-1):
                    return True
                return False
        return True