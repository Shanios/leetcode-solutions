class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
     avg_window_sum = sum(nums[:k])
     max_sum= avg_window_sum/k
     for fast in range(k,len(nums)):
        avg_window_sum = avg_window_sum + nums[fast] - nums[fast -k]

        max_sum = max(max_sum,avg_window_sum/k)
     return max_sum    
         