import math

def is_all_same_or_not(iitems):
    for i in range(len(iitems)-1):
        if iitems[i] != iitems[i+1]:
            return False
    
    return True

class Solution:
    def minimumSeconds(self, nums: list[int]):
        
        if is_all_same_or_not(nums):
            return 0
        
        dis_dict = {}
        dis_cal_dict = {}
        length  = len(nums)
        
        sec = math.ceil((length - 1) / 2)
        
        for i in range(length):
            if nums[i] not in dis_dict:
                dis_dict[nums[i]] = [i]
                
            else:
                dis_dict[nums[i]].append(i)
                
                if nums[i] not in dis_cal_dict:
                    dis_cal_dict[nums[i]] = [(dis_dict[nums[i]][-1] - dis_dict[nums[i]][-2] - 1)]
                else:
                    dis_cal_dict[nums[i]].append(dis_dict[nums[i]][-1] - dis_dict[nums[i]][-2] - 1)
            
        for item, dis_list in dis_dict.items():
            if len(dis_list) > 1:
                
                dis_cal_dict[item].append(length - (dis_list[-1] - dis_list[0] - 1) - 2)
                
        for item, dis_list in dis_cal_dict.items():
            if len(dis_list) > 1:
                count = math.ceil(max(dis_list) / 2)
                
                if count < sec:
                    sec = count
            
        return sec
    
if __name__ == '__main__':
    nums = [2,15,12,9,9,9]
    s = Solution()
    print(Solution().minimumSeconds(nums))