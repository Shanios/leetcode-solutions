class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = sum(nums[::])
        target =0
        for fast in range(0,len(nums)):
            target = max(nums[fast],target+nums[fast])
            max_sum = max(max_sum,target)
        return max_sum      