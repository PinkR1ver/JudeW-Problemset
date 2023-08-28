import numpy as np
from collections import Counter
import math

def is_all_same_or_not(iitems):
    for i in range(len(iitems)-1):
        if iitems[i] != iitems[i+1]:
            return False
    
    return True

def count_elements(items):
    counter = Counter(items)
    result = dict(counter)
    return result

def find_positions(lst, num):
    positions = [index for index, value in enumerate(lst) if value == num]
    return positions


def calculate_distances(positions, length):
    distances = [positions[i+1] - positions[i] - 1 for i in range(len(positions)-1)]
    distances.append(length - (positions[-1] - positions[0] - 1) - 2)
    return distances


class Solution:
    def minimumSeconds(self, nums: list[int]):
        
        if is_all_same_or_not(nums):
            return 0
        
        n = len(nums)
        
        unique_nums = count_elements(nums)
        unique_nums = dict(sorted(unique_nums.items(), key=lambda item: item[1], reverse=True))

        
        sec = math.ceil((n - 1) / 2)
        
        for element, count in unique_nums.items():
            
            if count == 1:
                break
            
            position = find_positions(nums, element)
            distances = calculate_distances(position, n)
            
            count = math.ceil(max(distances) / 2)
            
            if count < sec:
                sec = count
                
        return sec
            
            

if __name__ == '__main__':
    nums = [2,1,3,3,2]
    s = Solution()
    print(Solution().minimumSeconds(nums))