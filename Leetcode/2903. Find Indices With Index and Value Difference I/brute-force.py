import numpy as np

class Solution:
    def findIndices(self, nums: list[int], indexDifference: int, valueDifference: int) -> list[int]:
        for i in range(len(nums) - indexDifference):
            for j in range(i + indexDifference, len(nums)):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
                
        return [-1, -1]

if __name__ == '__main__':
    
    s = Solution()
    nums = [5, 1, 4, 1]
    indexDifference = 2
    valueDifference = 4
    
    print(s.findIndices(nums, indexDifference, valueDifference))
    