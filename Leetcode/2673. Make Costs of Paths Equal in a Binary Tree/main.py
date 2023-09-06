import math

class Solution:
    def minIncrements(self, n: int, cost: list[int]):
        
        ans = 0
        
        for i in range(int(math.log2(n+1)), 1, -1):
            for j in range(2** (i -1) - 1, 2 ** i - 1, 2):
                ans += abs(cost[j] - cost[j+1])
                cost[j] = max(cost[j], cost[j+1])
                cost[j+1] = cost[j]
                cost[int((j - 1) / 2)] += cost[j]
        
        return ans                
            
                  

if __name__ == '__main__':
    n = 7
    cost = [1,5,2,2,3,3,1]
    s = Solution()
    
    ans = s.minIncrements(n, cost)
    print(ans)