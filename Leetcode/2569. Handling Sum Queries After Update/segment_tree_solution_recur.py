import numpy as np

class Solution:   
    
    def handleQuery(self, nums1: list[int], nums2: list[int], queries: list[list[int]]):
        
        nums1, nums2 = np.array(nums1), np.array(nums2)
        ans = []
        
        tree = np.zeros(4 * len(nums1))
        n = len(nums1)
        segment_tree_build(tree, 0, nums2, 0, n - 1)
        
        
        for query in queries:
            if query[0] == 1:
                nums1[query[1]: query[2]+1] ^= 1

            if query[0] == 2:
                for i in range(n):
                    segment_tree_update(tree, 0, nums2, 0, n - 1, i, nums1[i] * query[1])
                
            if query[0] == 3:
                ans.append(int(tree[0]))
                
        return ans
        
    
def segment_tree_build(tree, node, nums, start, end):

    if start == end:
        tree[node] = nums[start]
    else:
        mid = (start + end) // 2
        segment_tree_build(tree, (2 * (node + 1)) - 1, nums, start, mid)
        segment_tree_build(tree, 2 * (node + 1), nums, mid + 1, end)    
        tree[node] = tree[(2 * (node+1)) - 1] + tree[2 * (node+1)]
        
def segment_tree_update(tree, node, nums, start, end, idx, val):
    if start == end:
        
        nums[idx] += val
        tree[node] += val
        
    else:
        mid = (start + end) // 2
        if start <= idx and idx <= mid:
            segment_tree_update(tree, (2 * (node+1)) - 1, nums, start, mid, idx, val)
        else:
            segment_tree_update(tree, 2 * (node+1), nums, mid + 1, end, idx, val)
            
        tree[node] = tree[(2 * (node+1)) - 1] + tree[2 * (node+1)]


if __name__ == '__main__':
    nums1 = [1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,0,1,0,1,1,0,1,0,1,0,1,0,0]
    nums2 = [48,2,32,25,30,37,32,18,48,39,34,19,46,43,30,22,20,35,28,3,5,45,39,21,46,45,12,15]
    queries = [[3,0,0],[2,3,0],[1,10,26],[2,4,0],[2,18,0]]
    
    s = Solution()
    print(s.handleQuery(nums1, nums2, queries))