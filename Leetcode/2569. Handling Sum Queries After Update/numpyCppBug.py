import numpy as np

class Solution:
    def handleQuery(self, nums1: list[int], nums2: list[int], queries: list[list[int]]):
        
        nums1, nums2 = np.array(nums1), np.array(nums2)
        n = len(nums1)
        ans = []
        
        for query in queries:
            if query[0] == 1:
                nums1[query[1]: query[2]+1] ^= 1

            if query[0] == 2:
                nums2 += nums1 * query[1]
                
            if query[0] == 3:
                ans.append(int(nums2.sum()))
                
        return ans

if __name__ == '__main__':
    nums1 = [1,0,1]
    nums2 = [0,0,0]
    queries = [[1,1,1],[2,1,0],[3,0,0]]
    
    s = Solution()
    print(s.handleQuery(nums1, nums2, queries))