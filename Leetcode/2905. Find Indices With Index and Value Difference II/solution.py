class Solution:
    def findIndices(self, nums: list[int], indexDifference: int, valueDifference: int) -> list[int]:
        min_flag = 0
        max_flag = 0
        
        for i in range(indexDifference, len(nums)):
            
            if nums[i - indexDifference] < nums[min_flag]:
                min_flag = i - indexDifference
            
            if nums[i - indexDifference] > nums[max_flag]:
                max_flag = i - indexDifference
                
            if nums[i] - nums[min_flag] >= valueDifference:
                return [min_flag, i]
            
            if nums[max_flag] - nums[i] >= valueDifference:
                return [max_flag, i]
            
        return [-1, -1]
            
        
                
if __name__ == '__main__':
    
    s = Solution()
    nums = [5, 1, 4, 1]
    indexDifference = 2
    valueDifference = 4
    
    print(s.findIndices(nums, indexDifference, valueDifference))
    