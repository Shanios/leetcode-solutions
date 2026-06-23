class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = 0
        max_len = 0
        seen = set()
        for fast in range(len(s)):
            while s[fast] in seen:
                seen.remove(s[slow])
                slow +=1
            seen.add(s[fast]) 
            max_len = max(max_len,fast-slow+1)
        return max_len    


        