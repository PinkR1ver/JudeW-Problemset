# Don't use numpy to test orginal python speed

class Solution:
    def handleQuery(self, nums1: list[int], nums2: list[int], queries: list[list[int]]):
        ans = []
        tree = SegTree(nums1)
        total2 = sum(nums2)
        
        for query in queries:
            if query[0] == 1:
                tree.zero_one_reverse(1, query[1], query[2])
            elif query[0] == 2:
                total1 = tree.tree[1].sum 
                total2 += total1 * query[1]
            elif query[0] == 3:
                ans.append(total2)
                
            print('Tree:', 'Query:', query)
            
            for i in range(1, tree.n * 4):
                print('node:', i, 'L:', tree.tree[i].l, 'R:', tree.tree[i].r, 'Sum:', tree.tree[i].sum, 'Lazy:', tree.tree[i].lazyTag)
        
            print('\n\n\n')
            
        return ans
    
       
class SegTree():
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.tree = [SegNode(-1, -1, 0 ,0) for _ in range(self.n * 4 + 1)]
        self.build(1, 0, self.n - 1)
        
    def build(self, idx, l, r):
        
        self.tree[idx] = SegNode(l, r, 0, 0)
        if l == r:
            self.tree[idx].sum = self.arr[l]
            return
        
        mid = (l + r) >> 1
        self.build(2 * idx, l, mid)
        self.build(2 * idx + 1, mid + 1, r)
        
        self.tree[idx].sum = self.tree[2 * idx].sum + self.tree[2 * idx + 1].sum
    
    def zero_one_reverse(self, idx, l, r):
        if self.tree[idx].l >= l and self.tree[idx].r <= r:
            if odd_or_even(self.tree[idx].lazyTag) == 0:
                self.tree[idx].sum = self.tree[idx].r - self.tree[idx].l + 1 - self.tree[idx].sum
            
            self.tree[idx].lazyTag = 0
            
            if not self.tree[idx].l == self.tree[idx].r:
                self.tree[2 * idx].lazyTag += 1
                self.tree[2 * idx + 1].lazyTag += 1
            
            return
        
        
        if self.tree[2 * idx].r  >= l and self.tree[2 * idx].r != -1:
            
            if odd_or_even(self.tree[idx].lazyTag) == 1:
                self.tree[idx].sum = self.tree[idx].r - self.tree[idx].l + 1 - self.tree[idx].sum
                self.tree[idx].lazyTag = 0
                
                if not self.tree[idx].l == self.tree[idx].r:
                    self.tree[2 * idx].lazyTag += 1
                    self.tree[2 * idx + 1].lazyTag += 1
                 
                 
            self.zero_one_reverse(2 * idx, l, r)
                
        if self.tree[2 * idx + 1].l <= r and self.tree[2 * idx + 1].l != -1:
            
            if odd_or_even(self.tree[idx].lazyTag) == 1:
                self.tree[idx].sum = self.tree[idx].r - self.tree[idx].l + 1 - self.tree[idx].sum
                self.tree[idx].lazyTag = 0
                 
                if not self.tree[idx].l == self.tree[idx].r:
                    self.tree[2 * idx].lazyTag += 1
                    self.tree[2 * idx + 1].lazyTag += 1
                 
            self.zero_one_reverse(2 * idx + 1, l, r)
            
        
        self.tree[idx].sum = self.tree[2 * idx].sum + self.tree[2 * idx + 1].sum

class SegNode():
    def __init__(self, l, r, sum, lazyTag):
        self.l = l
        self.r = r
        self.sum = sum
        self.lazyTag = lazyTag
        
def odd_or_even(num):
    if num % 2 == 0:
        return 0
    else:
        return 1
        
if __name__ == '__main__':
    nums1 = [1,0,1]
    nums2 = [44,28,35]
    queries = [[1,0,1],[2,10,0],[2,2,0],[2,7,0],[3,0,0],[3,0,0],[1,2,2],[1,1,2],[2,1,0],[1,0,2],[1,2,2],[1,0,2],[3,0,0],[1,1,2],[3,0,0],[1,0,1],[2,21,0],[1,0,1],[2,26,0],[1,1,1]]
    
    s = Solution()
    ans = s.handleQuery(nums1, nums2, queries)
    
    print(ans)
