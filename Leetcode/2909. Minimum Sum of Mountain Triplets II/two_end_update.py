class Solution:
    def minimumSum(self, nums: list[int]) -> int:
        
        min_sum = -1
        
        left = [nums[0]] * len(nums)
        right = [nums[-1]] * len(nums)
        
        for i in range(1, len(nums)):
            left[i] = min(left[i - 1], nums[i])
        for j in range(len(nums)-2, -1, -1):
            right[j] = min(right[j + 1], nums[j])
            
        for i in range(1, len(nums) - 1):
            if nums[i] > left[i - 1] and nums[i] > right[i + 1]:
                sum = nums[i] + left[i - 1] + right[i + 1]
                if min_sum == -1 or sum < min_sum:
                    min_sum = sum
                    
        return min_sum