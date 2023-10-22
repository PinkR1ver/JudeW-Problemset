from math import ceil
from collections import Counter

class Solution:
    def minGroupsForValidAssignment(self, nums: list[int]) -> int:
        
        ans = -1
        c = Counter(nums)
        
        if len(c) == 1:
            return 1
        
        for i in range(1, min(c.values()) + 1):
            
            tmp = 0
            okay = 1
            
            for key in c.keys():
                x = c[key] % i
                y=  c[key] // i
                
                if x > y:
                    okay = 0
                    break
            
                tmp += ceil(c[key] / (i + 1))
            
            if not okay:
                continue
            
            if ans == -1 or tmp < ans:
                ans = tmp
                
        return ans
        
    
if __name__ == '__main__':
    
    nums = [3,2,3,2,3]
    s = Solution()
    
    print(s.minGroupsForValidAssignment(nums))
     