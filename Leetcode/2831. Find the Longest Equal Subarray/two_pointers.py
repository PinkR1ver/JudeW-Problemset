class Solution:
    def longestEqualSubarray(self, nums: list[int], k: int) -> int:
        
        frequency = {}
        
        right = 0
        left = 0
        ans = 0
        
        frequency[nums[left]] = frequency.get(nums[left], 0) + 1
        max_flag = 0
        max_distinct = 0
        
        while True:
            
            if max_distinct < frequency[nums[right]]:
                max_distinct = frequency[nums[right]]
                max_flag = nums[right]
                
            slide_window = right - left + 1
            
            ans = max(ans, max_distinct)
            
            delete_element_num = slide_window - max_distinct
            
            if delete_element_num > k:
                frequency[nums[left]] -= 1
                
                if nums[left] == max_flag:
                    max_distinct -= 1
                
                left += 1
                
            if right == len(nums) - 1:
                break
            
            right += 1
            frequency[nums[right]] = frequency.get(nums[right], 0) + 1
            
        return ans
                
    
if __name__ == '__main__':
    
    nums = [1]
    k = 0
    
    
    s = Solution()
    print(s.longestEqualSubarray(nums, k))