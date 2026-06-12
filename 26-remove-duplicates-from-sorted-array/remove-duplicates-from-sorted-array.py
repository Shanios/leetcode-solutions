class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        counter =0
        while fast < len(nums):
         if nums[fast] != nums[slow]:
          nums[slow+1] = nums[fast]
          slow +=1
          fast +=1
          counter +=1
         else:
          fast += 1 
        nums[slow+1 : len(nums)] = ["_"] * (len(nums) - (slow + 1))    
        return slow + 1     