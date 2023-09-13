class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.n = len(nums)
        self.tree = [0] * (self.n * 2 + 1)
        
        for i in range(self.n):
            self.tree[i + self.n] = nums[i]
            
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
        
        

    def update(self, index: int, val: int):
        
        index += self.n
        self.tree[index] = val
        
        while index > 1:
            index //= 2
            self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]
                     
            
        
        

    def sumRange(self, left: int, right: int):
        
        left += self.n
        right += self.n
        summery = 0

        while left <= right:
            if left % 2 == 1:
                summery += self.tree[left]
                left += 1
            
            if right % 2 == 0:
                summery += self.tree[right]
                right -= 1
            
            left //= 2
            right //= 2
            
        return summery

    

if __name__ == "__main__":
    pass
    
