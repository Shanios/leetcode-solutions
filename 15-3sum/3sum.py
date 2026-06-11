class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        result =[]
        nums.sort()
        for fixed_num in range(len(nums)):
            if fixed_num > 0 and nums[fixed_num] == nums[fixed_num - 1]:
                continue 
            left = fixed_num + 1
            right = len(nums) - 1
            while left < right:
             if nums[fixed_num] + nums[left] + nums[right] > 0:
                right -=1
             elif nums[fixed_num] + nums[left] + nums[right] <0:    
                left +=1 
             else:
                result.append(
                [nums[fixed_num], nums[left], nums[right]]
                  )           
                
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                   left += 1
                while left < right and nums[right] == nums[right + 1]:
                   right -= 1

        return result
        

        