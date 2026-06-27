class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set()
        
        for fast in range(0,len(nums)):
         
          if nums[fast] in seen:
            return True
          else:
           seen.add(nums[fast]) 
        return False    
            

