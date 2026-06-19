class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c for c in s if c.isalnum()]
        s = [c.lower() for c in s if c.isalnum()]
        s   ="".join([c for c in s])
        left =0
        right = len(s)-1
        while left <= right:
            if s[left] == s[right] or len(s) ==0:
                left +=1
                right -=1
            else:
             return False    

        return True