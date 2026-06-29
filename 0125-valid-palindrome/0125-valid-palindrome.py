import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]',"",s).lower()
        slow = 0
        fast = len(s) -1
        while fast >slow:
            if s[fast] == s[slow]:
                slow +=1
                fast -=1
            else:
                return False
        return True            
        
        