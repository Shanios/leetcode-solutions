class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        slow =  0
        nums.sort()
        
        for fast in range(1,len(nums)):
         
          if nums[fast] == nums[slow]:
            return True
          else:
           fast +=1  
          slow +=1  
        return False    
            

